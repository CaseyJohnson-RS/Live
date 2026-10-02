---
hide:
  - navigation
  - toc
  - footer
---

<script>
/* Монитор включается, когда главную открыли заново или перезагрузили.
   Не включается при переходе с другой страницы сайта и по «Назад»: там
   экран уже горит. И никогда — если посетитель отключил анимацию.
   Стоит в начале страницы, чтобы включённый экран не мелькнул заранее */
(function () {
  try {
    var nav = performance.getEntriesByType("navigation")[0];
    var type = nav ? nav.type : "navigate";
    var fromSite = false;
    try {
      fromSite = !!document.referrer &&
        new URL(document.referrer).origin === location.origin;
    } catch (e) {}
    var boot = type === "reload" || (type === "navigate" && !fromSite);
    if (boot && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
      document.documentElement.classList.add("crt-boot");
    }
  } catch (e) {}
})();
</script>

<svg class="crt__defs" aria-hidden="true">
<filter id="crt-barrel" x="0" y="0" width="1" height="1" primitiveUnits="objectBoundingBox" color-interpolation-filters="sRGB">
<feImage href="assets/crt/barrel-map.png" x="0" y="0" width="1" height="1" preserveAspectRatio="none" result="map"/>
<feDisplacementMap in="SourceGraphic" in2="map" scale="0.1" xChannelSelector="R" yChannelSelector="G"/>
</filter>
</svg>

<div class="stage" markdown>

<img class="table-layer table-layer--back" src="assets/table-back.svg" alt="" aria-hidden="true">

<div class="intro crt" markdown>

<div class="crt__image" markdown>

<p class="status"><span class="status__dot" aria-hidden="true"></span>В разработке</p>

<div class="hero" markdown>

<div class="hero__logo"><span class="hero__rec" aria-hidden="true"></span><img src="logo.svg" alt="Live"></div>

<p class="hero__tagline">Игра по мотивам русской рулетки</p>

</div>

<div class="teaser">
<p>Садятся несколько — встаёт один.</p>
<p>Выстрел в себя покупает будущее.</p>
<p>Каждый хочет обмануть.</p>
<p class="teaser__call">Наблюдай. Считай. Рискуй.</p>
<p class="teaser__coda">Удачи.</p>
</div>

</div>

</div>

<img class="table-layer table-layer--front" src="assets/table-front.svg" alt="" aria-hidden="true">

</div>

## Ставки пока не принимаются

Зал ещё закрыт.

Движок в разработке, клиент — в планах. Но что это за игра можно узнать уже сейчас, а когда откроются двери — следить в блоге.

[:octicons-arrow-right-24: Об игре](about/index.md){ .md-button .md-button--primary }
[:octicons-arrow-right-24: Открыть блог](blog/index.md){ .md-button }

## Проект

<div class="grid cards project" markdown>

-   :live-cartridge:{ .chip-emblem } **Об игре**

    ---

    Описание игры, иллюстрации, правила.

    [:octicons-arrow-right-24: Читать](about/index.md)

-   :material-engine-outline:{ .chip-emblem } **Движок**

    ---

    Логический движок игры, который будет держать игру и контролировать выполнения правил. В данный момент разрабатывается.

    [:octicons-mark-github-16: LiveEngine](https://github.com/CaseyJohnson-RS/LiveEngine) ·
    [документация](https://caseyjohnson-rs.github.io/LiveEngine/)

-   :material-monitor-dashboard:{ .chip-emblem } **Клиент**

    ---

    Сама игра. Возможно, здесь будет ссылка на стим или Itch.io в будущем.

    *В планах*

-   :material-timeline-text-outline:{ .chip-emblem } **Блог**

    ---

    Как проект движется от идеи к релизу:
    хронология и рассказы о вехах.

    [:octicons-arrow-right-24: Открыть блог](blog/index.md)

</div>

## Вдохновение и истоки

<div class="roots">

<figure class="root">
<a href="https://en.wikipedia.org/wiki/Buckshot_Roulette"><img src="assets/references/buckshot-roulette.jpg" style="object-position: right" alt="Обложка Buckshot Roulette" loading="lazy"></a>
<figcaption>
<span class="root__title">Buckshot Roulette</span>
<span class="root__text">Рулетка за столом против соперника: выстрел в себя или в него, предметы, которые переворачивают расклад.</span>
<span class="root__credit">© Mike Klubnika, Critical Reflex</span>
</figcaption>
</figure>

<figure class="root">
<a href="https://en.wikipedia.org/wiki/Inscryption"><img src="assets/references/inscryption.jpg" alt="Обложка Inscryption" loading="lazy"></a>
<figcaption>
<span class="root__title">Inscryption</span>
<span class="root__text">Мрачный стол под одной лампой, за которым ставка — ты сам.</span>
<span class="root__credit">© Daniel Mullins Games, Devolver Digital</span>
</figcaption>
</figure>

<figure class="root">
<a href="https://en.wikipedia.org/wiki/Routine_(video_game)"><img src="assets/references/routine.png" alt="Обложка Routine" loading="lazy"></a>
<figcaption>
<span class="root__title">Routine</span>
<span class="root__text">Будущее, каким его видели в восьмидесятые: холодный свет ЭЛТ-мониторов и хром.</span>
<span class="root__credit">© Lunar Software, Raw Fury</span>
</figcaption>
</figure>

</div>

<script>
/* Включение стартует, когда страница загрузилась (шрифты, логотип),
   но не позже чем через 2,5 с. После — экран в обычном режиме */
(function () {
  var root = document.documentElement;
  if (!root.classList.contains("crt-boot")) return;
  var started = false;
  function powerOn() {
    if (started) return;
    started = true;
    root.classList.add("crt-boot--go");
  }
  var screen = document.querySelector(".crt__image");
  if (screen) {
    screen.addEventListener("animationend", function (e) {
      if (e.animationName === "crt-power-on") {
        root.classList.remove("crt-boot", "crt-boot--go");
      }
    });
  }
  if (document.readyState === "complete") powerOn();
  else window.addEventListener("load", powerOn);
  setTimeout(powerOn, 2500);
})();

/* При уходе со страницы монитор гаснет. Пока грузится следующая страница
   (и при перезагрузке), браузер держит последний кадр старой — пусть на
   нём будет тёмное стекло, а не горящий экран. Если ухода не случилось
   (например, клик по ссылке на почту), через 1,5 с экран загорается снова */
window.addEventListener("beforeunload", function () {
  var root = document.documentElement;
  root.classList.add("crt-off");
  setTimeout(function () { root.classList.remove("crt-off"); }, 1500);
});
</script>
