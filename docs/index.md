---
hide:
  - navigation
  - toc
  - footer
---

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

Зал ещё закрыт: движок в разработке, клиент — в планах. Но как здесь
играют, можно узнать уже сейчас, а когда откроются двери — следить в
блоге.

[:octicons-arrow-right-24: Как играть](rules/index.md){ .md-button .md-button--primary }
[:octicons-arrow-right-24: Открыть блог](blog/index.md){ .md-button }

## Проект

<div class="grid cards project" markdown>

-   :material-book-open-variant:{ .chip-emblem } **Как играть**

    ---

    Полный свод правил: читается по порядку, от первой главы до
    последней.

    [:octicons-arrow-right-24: Читать](rules/index.md)

-   :material-engine-outline:{ .chip-emblem } **Движок**

    ---

    Сервер игры на Python: держит партию и честно применяет правила.
    Клиенты подключаются к нему по WebSocket.

    [:octicons-mark-github-16: LiveEngine](https://github.com/CaseyJohnson-RS/LiveEngine) ·
    [документация](https://caseyjohnson-rs.github.io/LiveEngine/)

-   :material-monitor-dashboard:{ .chip-emblem } **Клиент**

    ---

    Приложение, за которым сидит игрок: стол, ряд, предметы.

    *В планах*

-   :material-timeline-text-outline:{ .chip-emblem } **Блог**

    ---

    Как проект движется от идеи к столу, за которым можно сыграть:
    хронология и рассказы о вехах.

    [:octicons-arrow-right-24: Открыть блог](blog/index.md)

</div>

## Корни

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
