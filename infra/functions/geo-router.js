// CloudFront Function — /es (ES), / (EN), geo redirect LATAM → /es
var LATAM = [
  'MX', 'CO', 'AR', 'PE', 'VE', 'CL', 'EC', 'GT', 'CU',
  'BO', 'DO', 'HN', 'PY', 'SV', 'NI', 'CR', 'PA', 'UY',
];

function redirectTo(path) {
  return {
    statusCode: 302,
    statusDescription: 'Found',
    headers: {
      location: { value: path },
    },
  };
}

function langCookie(request) {
  var cookies = request.cookies;
  if (cookies['cf_lang'] && cookies['cf_lang'].value) {
    return cookies['cf_lang'].value;
  }
  return '';
}

function handler(event) {
  var request = event.request;
  var uri = request.uri;
  var pref = langCookie(request);

  // /es → sirve index.html (URL visible sigue siendo /es)
  if (uri === '/es' || uri === '/es/') {
    request.uri = '/index.html';
    return request;
  }
  if (uri.indexOf('/es/') === 0) {
    request.uri = '/index.html';
    return request;
  }

  // Homepage: respetar preferencia o geo LATAM → /es
  if (uri === '/' || uri === '/index.html') {
    if (pref === 'es') {
      return redirectTo('/es');
    }
    if (pref === 'en') {
      return request;
    }
    var country = event.viewer.country || '';
    if (LATAM.indexOf(country) > -1) {
      return redirectTo('/es');
    }
  }

  return request;
}
