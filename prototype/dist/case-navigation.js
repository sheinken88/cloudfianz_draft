/* Progressive enhancement: native chapter links remain usable without JS. */
(() => {
  const navigation = document.querySelector('.story-navigation');
  const story = document.querySelector('.case-story');
  const header = document.querySelector('.site-header');
  if (!navigation || !story || !header) return;

  const chapters = [...navigation.querySelectorAll('a[href^="#"]')]
    .map(link => ({link, section: document.getElementById(link.hash.slice(1))}))
    .filter(chapter => chapter.section);
  const desktop = matchMedia('(min-width: 800px)');
  let queued = false;

  function update() {
    queued = false;
    const headerBottom = header.getBoundingClientRect().bottom;
    const navBounds = navigation.getBoundingClientRect();
    const storyBottom = story.getBoundingClientRect().bottom;
    navigation.classList.toggle('is-stuck', desktop.matches &&
      navBounds.top <= headerBottom + 1 && storyBottom > headerBottom);

    const readingLine = headerBottom + (desktop.matches ? navBounds.height : 0) + 64;
    let current;
    for (const chapter of chapters) {
      if (chapter.section.getBoundingClientRect().top <= readingLine) current = chapter.link;
    }
    if (storyBottom <= headerBottom) current = undefined;
    for (const {link} of chapters) {
      if (link === current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
  }

  function scheduleUpdate() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(update);
  }

  window.addEventListener('scroll', scheduleUpdate, {passive: true});
  window.addEventListener('resize', scheduleUpdate);
  window.addEventListener('pageshow', scheduleUpdate);
  window.addEventListener('load', scheduleUpdate);
  desktop.addEventListener('change', scheduleUpdate);
  update();
})();
