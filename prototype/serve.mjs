// Local preview: explicit page routes, stable URLs and real 404 responses.
import http from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('./dist/', import.meta.url));
const pageRoutes = JSON.parse(await readFile(new URL('./page-routes.json', import.meta.url), 'utf8'));
const pages = new Map([['/es', 'index.html'], ...Object.values(pageRoutes).map(route => [route, `${route.slice(1)}/index.html`])]);
const aliases = new Map([['/', '/es'], ['/index.html', '/es'], ['/es/index.html', '/es']]);
for (const route of pages.keys()) {
  aliases.set(`${route}/`, route);
  aliases.set(`${route}/index.html`, route);
}
const types = {'.html':'text/html; charset=utf-8', '.css':'text/css; charset=utf-8', '.js':'text/javascript; charset=utf-8', '.json':'application/json; charset=utf-8', '.png':'image/png', '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.svg':'image/svg+xml', '.webp':'image/webp', '.avif':'image/avif', '.ico':'image/x-icon'};
const notFound = '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><meta name="robots" content="noindex,nofollow"><title>Página no encontrada | Cloudfianz</title><link rel="stylesheet" href="/styles.css"><main class="container section-pad"><p>Cloudfianz</p><h1 style="font-size:42px;margin:24px 0">No encontramos esa página.</h1><p>Podés volver al inicio para explorar nuestros servicios y proyectos.</p><a class="button" href="/es" style="margin-top:30px">Volver al inicio</a></main></html>';
const server = http.createServer(async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex, nofollow');
  res.setHeader('X-Content-Type-Options', 'nosniff');
  const send = (status, body, type='text/html; charset=utf-8') => {
    res.writeHead(status, {'Content-Type':type});
    res.end(req.method === 'HEAD' ? undefined : body);
  };
  if (!['GET','HEAD'].includes(req.method)) {
    res.setHeader('Allow', 'GET, HEAD');
    return send(405, 'Method not allowed', 'text/plain; charset=utf-8');
  }
  const [rawPath, query] = (req.url || '/').split(/\?(.*)/s);
  let pathname;
  try { pathname = decodeURIComponent(rawPath); } catch { return send(400, 'Invalid URL', 'text/plain; charset=utf-8'); }
  if (pathname.includes('\\') || pathname.includes('\0') || pathname.split('/').some(part => part.startsWith('.'))) return send(404, notFound);
  if (aliases.has(pathname)) {
    res.writeHead(301, {Location: aliases.get(pathname) + (query ? `?${query}` : '')});
    return res.end();
  }
  if (pathname === '/robots.txt') return send(200, 'User-agent: *\nDisallow: /\n', 'text/plain; charset=utf-8');
  const file = path.resolve(root, pages.get(pathname) || `.${pathname}`);
  if (!file.startsWith(root) || !types[path.extname(file)]) return send(404, notFound);
  try {
    if (!(await stat(file)).isFile()) return send(404, notFound);
    return send(200, await readFile(file), types[path.extname(file)]);
  } catch (error) {
    if (['ENOENT', 'ENOTDIR'].includes(error.code)) return send(404, notFound);
    console.error('Local preview failed to read a file:', error.code);
    return send(500, 'Preview unavailable', 'text/plain; charset=utf-8');
  }
});
server.on('error', error => { console.error(error.message); process.exitCode = 1; });
server.listen(3001, '127.0.0.1', () => console.log('Cloudfianz preview: http://127.0.0.1:3001/review.html'));
