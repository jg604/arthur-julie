import re, sys
src = open('index.html', encoding='utf-8').read()
out = src
def rep(old, new, count=1):
    global out
    n = out.count(old)
    assert n == count, f"expected {count} occurrence(s) of {old[:60]!r}, found {n}"
    out = out.replace(old, new)

# ---------- head ----------
rep('<html lang="en">', '<html lang="hy">')
rep('<title>Arthur &amp; Julie — Wedding Invitation</title>', '<title>Արթուր &amp; Ջուլի — Հարսանեկան հրավեր</title>')
rep('content="Arthur & Julie invite you to celebrate their wedding — 01.11.2026"',
    'content="Արթուրն ու Ջուլին հրավիրում են Ձեզ իրենց հարսանիքին — 01.11.2026"')
rep('family=Tangerine:wght@700&display=swap', 'family=Tangerine:wght@700&family=Noto+Serif+Armenian:wght@300;400;500;600&display=swap')

# ---------- Armenian typography overrides ----------
hy_css = r'''
/* ---------- Armenian typography ---------- */
:root{
  --hy:'Noto Serif Armenian',Georgia,serif;
  --serif:'Cormorant Garamond','Noto Serif Armenian',Georgia,serif;
  --body:'EB Garamond','Noto Serif Armenian',Georgia,serif;
}
.hscript{font-family:var(--hy);font-weight:300;font-size:28px;line-height:1.35;letter-spacing:.02em}
.hscript.big{font-size:31px}
.hscript.sm{font-size:25px}
.lead{font-size:16.5px;line-height:1.9}
.smallcaps{font-family:var(--hy);font-weight:500;font-size:10.5px;letter-spacing:.2em;text-indent:.2em;line-height:2.1}
.btn{font-family:var(--hy);font-weight:500;font-size:11px;letter-spacing:.16em;text-indent:.16em;padding:15px 30px}
.env-names .of{font-family:var(--hy);font-weight:500;font-size:10px;letter-spacing:.3em;text-indent:.3em}
.env-names h1{font-family:var(--hy);font-weight:300;font-size:36px;letter-spacing:.04em;margin-top:16px;line-height:1.2}
.env-names .amp{font-family:var(--script);font-size:54px;padding:0 4px;position:relative;top:3px;line-height:1}
.seal-hint{font-family:var(--hy);font-weight:500;font-size:10.5px;letter-spacing:.16em;text-indent:.16em}
.hero-names{font-family:var(--hy);font-weight:300;font-size:40px;letter-spacing:.04em;line-height:1.2}
.hero-names .amp{font-family:var(--script);font-size:60px;padding:0 6px;position:relative;top:3px;line-height:1}
.hero-sub{font-style:normal;font-size:15.5px;letter-spacing:.04em}
.cal-head .m{font-family:var(--hy);font-weight:300;font-size:24px;letter-spacing:.03em}
.cal-grid .dow{font-family:var(--hy);font-weight:500;font-size:9.5px;letter-spacing:.05em}
.v-name{font-family:var(--hy);font-weight:500;font-size:22px;letter-spacing:.1em;text-indent:.1em}
.v-lines{font-size:16px;line-height:1.9}
.tl2-row{grid-template-columns:78px 44px 1fr}
.tl2-line,#rose{left:100px}
.tl2-time{font-size:26px}
.tl2-label{font-family:var(--hy);font-weight:400;font-size:16px;line-height:1.4}
.tl2-label small{font-family:var(--hy);font-style:normal;font-weight:400;font-size:13px;letter-spacing:.01em}
.cd{gap:4px}
.cd>div:not(.sep){flex:0 0 66px}
.cd b{font-size:42px}
.cd small{font-family:var(--hy);font-weight:400;font-size:11.5px;letter-spacing:.03em;margin-top:10px}
.cd .sep{font-size:36px;padding:0 2px}
.rsvp-deadline{font-style:normal;font-size:15px;letter-spacing:.02em}
.f-label{font-size:16px}
.choice{font-size:16px;line-height:1.5}
.f-input,.f-area{font-size:16px}
.f-input::placeholder,.f-area::placeholder{color:#a89a7d}
.thanks-title{font-family:var(--hy);font-weight:300;font-size:30px;color:#a5813a;letter-spacing:.02em}
.foot-love{font-family:var(--hy);font-weight:300;font-size:20px;letter-spacing:.03em}
.foot-love .amp{font-family:var(--script);font-size:30px;padding:0 2px;position:relative;top:1px;line-height:1}
@media (max-width:380px){
  .hscript{font-size:26px}.hscript.big{font-size:29px}.hscript.sm{font-size:23px}
  .hero-names{font-size:36px}.hero-names .amp{font-size:54px}
  .env-names h1{font-size:33px}.env-names .amp{font-size:50px}
  .cd>div:not(.sep){flex:0 0 60px}.cd b{font-size:36px}.cd .sep{font-size:32px}.cd small{font-size:10.5px}
  .v-name{font-size:20px}
  .hero-date{font-size:19px;gap:12px;white-space:nowrap}.hero-date::before,.hero-date::after{width:30px}
}
</style>'''
rep('</style>', hy_css)

# ---------- envelope ----------
rep('<div class="of">The Wedding of</div>', '<div class="of">Հարսանեկան հրավեր</div>')
rep('<h1>Arthur <span class="amp">&amp;</span> Julie</h1>', '<h1>Արթուր <span class="amp">&amp;</span> Ջուլի</h1>')
rep('aria-label="Open the invitation"', 'aria-label="Բացել հրավերը"')
rep('<span class="seal-hint">tap the seal to open</span>', '<span class="seal-hint">սեղմեք կնիքին՝ բացելու համար</span>')

# ---------- hero ----------
rep('<div class="hero-names rv">Arthur <span class="amp">&amp;</span> Julie</div>',
    '<div class="hero-names rv">Արթուր <span class="amp">&amp;</span> Ջուլի</div>')
rep('Together with their families<br>invite you to their wedding',
    'Իրենց ընտանիքների հետ միասին<br>հրավիրում են Ձեզ<br>իրենց հարսանիքին')
rep('<div class="hero-sub rv d3">Sunday, the first of November</div>', '<div class="hero-sub rv d3">Կիրակի, նոյեմբերի 1</div>')

# ---------- invitation card ----------
rep('<div class="hscript">Dear Family &amp; Friends</div>', '<div class="hscript sm">Սիրելի հարազատներ<br>և ընկերներ</div>')
rep('<p class="lead">This autumn we begin a new chapter of our story. We would be honoured to have you beside us as we exchange our vows — and to raise a glass together at the celebration that follows.</p>',
    '<p class="lead">Սիրով հրավիրում ենք Ձեզ մեր հարսանեկան արարողությանը։ Այս օրն ամբողջական չի լինի առանց մեր սիրելի մարդկանց, և Ձեր ներկայությունը մեզ համար ամենաթանկ նվերն է։</p>')

# ---------- calendar ----------
rep('<div class="hscript rv">Save the Date</div>', '<div class="hscript rv">Նշեք այս օրը</div>')
rep('<span class="m">November</span>', '<span class="m">Նոյեմբեր</span>')
rep('<span class="dow">Mo</span><span class="dow">Tu</span><span class="dow">We</span><span class="dow">Th</span><span class="dow">Fr</span><span class="dow">Sa</span><span class="dow">Su</span>',
    '<span class="dow">Երկ</span><span class="dow">Երք</span><span class="dow">Չրք</span><span class="dow">Հնգ</span><span class="dow">Ուրբ</span><span class="dow">Շբթ</span><span class="dow">Կիր</span>')

# ---------- ceremony ----------
rep('<div class="hscript rv">The Ceremony</div>', '<div class="hscript rv">Պսակադրություն</div>')
rep('<div class="v-name">Saghmosavank</div>', '<div class="v-name">Սաղմոսավանք</div>')
rep('''      The wedding ceremony begins at <i>2:40</i><br>
      in the afternoon. We kindly ask<br>
      our guests to gather by <i>2:30</i>.''',
    '''      Պսակադրությունը կսկսվի ցերեկվա<br>
      ժամը <i>2:40</i>-ին։ Սիրով խնդրում ենք<br>
      հյուրերին հավաքվել մինչև ժամը <i>2:30</i>-ը։''')
rep('>View on the map</a>', '>Դիտել քարտեզում</a>', count=2)

# ---------- reception ----------
rep('<div class="hscript rv">The Celebration</div>', '<div class="hscript rv">Հարսանեկան խնջույք</div>')
rep('<div class="v-name">Latar Hall</div>', '<div class="v-name">Լաթառ</div>')
rep('''      The welcome reception opens at <i>5:00</i><br>
      in the evening, and at <i>5:30</i> we sit down<br>
      to the wedding banquet.''',
    '''      Հյուրերի դիմավորումը կսկսվի<br>
      երեկոյան ժամը <i>5:00</i>-ին, իսկ ժամը <i>5:30</i>-ին<br>
      կսկսվի հարսանեկան խնջույքը։''')

# ---------- timeline ----------
rep('<div class="hscript" style="margin-bottom:8px">Order of the Day</div>', '<div class="hscript" style="margin-bottom:8px">Օրվա ծրագիրը</div>')
rep('<div class="tl2-label">Guests gather<small>Saghmosavank Monastery</small></div>', '<div class="tl2-label">Հյուրերի հավաքը<small>Սաղմոսավանք</small></div>')
rep('<div class="tl2-label">The ceremony<small>the blessing of our marriage</small></div>', '<div class="tl2-label">Պսակադրություն</div>')
rep('<div class="tl2-label">Welcome reception<small>Latar Hall</small></div>', '<div class="tl2-label">Հյուրերի դիմավորում<small>Լաթառ</small></div>')
rep('<div class="tl2-label">The banquet<small>dinner, music &amp; dancing</small></div>', '<div class="tl2-label">Խնջույք<small>ընթրիք, երաժշտություն և պար</small></div>')

# ---------- countdown ----------
rep('<div class="hscript big rv">The Celebration<br>Begins In</div>', '<div class="hscript big rv">Մինչև հարսանիքը<br>մնաց</div>')
rep('<small>Days</small>', '<small>Օր</small>')
rep('<small>Hours</small>', '<small>Ժամ</small>')
rep('<small>Minutes</small>', '<small>Րոպե</small>')
rep('<small>Seconds</small>', '<small>Վայրկյան</small>')

# ---------- rsvp ----------
rep('<div class="hscript">Confirm Your Attendance</div>', '<div class="hscript">Հաստատեք<br>մասնակցությունը</div>')
rep('<p class="lead" style="max-width:320px">Please let us know whether you will be able to share the day with us.</p>',
    '<p class="lead" style="max-width:320px">Խնդրում ենք տեղեկացնել՝ կկարողանա՞ք արդյոք այս օրը կիսել մեզ հետ։</p>')
rep('<div class="rsvp-deadline">— kindly reply by the 1st of October —</div>', '<div class="rsvp-deadline">— խնդրում ենք պատասխանել<br>մինչև հոկտեմբերի 1-ը —</div>')
rep('<label class="f-label" for="fName">Your name &amp; surname</label>', '<label class="f-label" for="fName">Ձեր անունը և ազգանունը</label>')
rep('placeholder="e.g. Anna Petrosyan"', 'placeholder="օր.՝ Աննա Պետրոսյան"')
rep('<span class="f-label">Will you be able to join us?</span>', '<span class="f-label">Կկարողանա՞ք միանալ մեզ</span>')
rep('<span class="c-text">With great pleasure — we will be there</span>', '<span class="c-text">Մեծ ուրախությամբ՝ անպայման կլինենք</span>')
rep('<span class="c-text">Sadly, we will not be able to come</span>', '<span class="c-text">Ցավոք, չենք կարողանա ներկա լինել</span>')
rep('<label class="f-label" for="fGuests">Who is coming with you?</label>', '<label class="f-label" for="fGuests">Ո՞վ է գալու Ձեզ հետ</label>')
rep('placeholder="Please list everyone from your family who will join — and if you are bringing a plus one, add their name too"',
    'placeholder="Խնդրում ենք նշել Ձեր ընտանիքի բոլոր անդամներին, ովքեր կգան, իսկ եթե գալու եք զույգով՝ նշեք նաև նրա անունը"')
rep('          <div class="f-hint">Count everyone in — grown-ups, little ones, and your plus one alike.</div>\n', '')
rep('<button class="btn f-send" type="submit">Send reply</button>', '<button class="btn f-send" type="submit">Ուղարկել պատասխանը</button>')
rep('<div style="font-family:var(--script);font-size:44px;color:#a5813a">Thank you</div>', '<div class="thanks-title">Շնորհակալություն</div>')

# ---------- footer ----------
rep('<div class="foot-love rv d2">with love, Arthur &amp; Julie</div>', '<div class="foot-love rv d2">սիրով՝ Արթուր <span class="amp">&amp;</span> Ջուլի</div>')
rep('aria-label="Music on/off"', 'aria-label="Երաժշտություն"')

# ---------- js strings ----------
rep("? 'Your reply has reached us — we are so happy you will be there, and we can’t wait to celebrate with you.'",
    "? 'Ձեր պատասխանը հասել է մեզ։ Շատ ուրախ ենք, որ կլինեք մեզ հետ, և անհամբեր սպասում ենք միասին տոնելուն։'")
rep(": 'Thank you for letting us know. We will miss you dearly, and we will raise a glass in your honour.'",
    ": 'Շնորհակալ ենք, որ տեղեկացրիք։ Մեզ շատ կպակասեք, և մենք բաժակ կբարձրացնենք Ձեր պատվին։'")

open('hy.html', 'w', encoding='utf-8').write(out)
print('written', len(out))
