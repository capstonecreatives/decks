/* Capstone Creatives — sign in with a WhatsApp code before the page shows.
   Activated by setting LOGIN_URL (the Google Apps Script web-app URL). Empty = gate off. */
(function(){
  var LOGIN_URL = 'https://script.google.com/macros/s/AKfycbzdma2E_n8Dmq5NPYVKJUC2VrPt4RFEx0T4roa5nJa53CLK_HJUAPBvvysP_eclNZDhtw/exec';
  /* TEST_ONLY: the sign-in shows only on devices opened once with ?logintest (switch to false to go live for everyone) */
  var TEST_ONLY = true;
  try{ if(/[?&]logintest\b/.test(location.search)) localStorage.setItem('cl-test','1'); if(/[?&]logintest=off\b/.test(location.search)) localStorage.removeItem('cl-test'); }catch(e){}
  if (TEST_ONLY){ var _t=null; try{ _t=localStorage.getItem('cl-test'); }catch(e){} if(_t!=='1' && !window.__CL_URL) return; }
  var URL_ = (window.__CL_URL || LOGIN_URL || '').trim();
  if (!URL_) return;
  var KEY='cl-session', RECHECK_MS=12*3600*1000;
  var html=document.documentElement; html.classList.add('cl-locked');
  var css=document.createElement('style'); css.id='clGateCss';
  css.textContent='html.cl-locked body>*:not(#clGate){visibility:hidden!important}html.cl-locked{overflow:hidden}'+
  '#clGate{position:fixed;inset:0;z-index:2147483600;display:flex;align-items:center;justify-content:center;padding:24px;background:#0B2530;background:radial-gradient(120% 90% at 50% 0%,#0E4A5E 0%,#062836 55%,#03141C 100%);font-family:-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#F2F5F6}'+
  'html:not(.cl-locked) #clGate{display:none}'+
  '#clGate .cl-box{width:100%;max-width:360px;text-align:center}'+
  '#clGate .cl-brand{font-size:11px;font-weight:700;letter-spacing:.32em;text-transform:uppercase;color:#9CCBD2}'+
  '#clGate h1{margin:14px 0 6px;font-size:24px;font-weight:600;letter-spacing:-.01em;color:#fff}'+
  '#clGate p{margin:0 0 20px;color:#B9CDD2;font-size:14px;line-height:1.5}'+
  '#clGate .cl-row{display:flex;gap:8px}'+
  '#clGate select,#clGate input{height:52px;border-radius:12px;border:1.5px solid rgba(255,255,255,.25);background:rgba(255,255,255,.08);color:#fff;font-size:18px;padding:0 14px;box-sizing:border-box}'+
  '#clGate select{flex:none;width:104px;font-size:16px}#clGate select option{color:#000}'+
  '#clGate input{flex:1;min-width:0;width:100%}#clGate input::placeholder{color:rgba(255,255,255,.45)}'+
  '#clGate input.cl-code{text-align:center;letter-spacing:.5em;font-size:24px}'+
  '#clGate input:focus,#clGate select:focus{outline:none;border-color:#9CCBD2}'+
  '#clGate button.cl-go{margin-top:12px;width:100%;height:52px;border:0;border-radius:12px;background:#25D366;color:#06301A;font-size:16px;font-weight:700;cursor:pointer}'+
  '#clGate button.cl-go[disabled]{opacity:.6;cursor:default}'+
  '#clGate .cl-link{margin-top:14px;background:none;border:0;color:#9CCBD2;font-size:13.5px;cursor:pointer;text-decoration:underline;text-underline-offset:3px}'+
  '#clGate .cl-link[disabled]{opacity:.55;cursor:default;text-decoration:none}'+
  '#clGate .cl-msg{min-height:20px;margin-top:12px;font-size:13.5px;color:#FFD8A8}'+
  '#clGate .cl-foot{margin-top:26px;font-size:12px;color:rgba(255,255,255,.45)}'+
  '#clGate :focus-visible{outline:2px solid #9CCBD2;outline-offset:2px}';
  (document.head||html).appendChild(css);

  function store(){ try{ return JSON.parse(localStorage.getItem(KEY)||'null'); }catch(e){ return null; } }
  function save(s){ try{ localStorage.setItem(KEY,JSON.stringify(s)); }catch(e){} }
  function clear(){ try{ localStorage.removeItem(KEY); }catch(e){} }
  function unlock(){ html.classList.remove('cl-locked'); }
  function api(body){ return fetch(URL_,{method:'POST',body:JSON.stringify(body)}).then(function(r){ return r.json(); }); }
  window.capstoneSignOut=function(){ clear(); location.reload(); };

  var s=store(), now=Date.now();
  if (s && s.token && s.exp*1000>now){
    if (now-(s.checked||0)<RECHECK_MS){ unlock(); return; }
    api({action:'check',token:s.token}).then(function(r){
      if (r&&r.ok){ s.checked=Date.now(); s.name=r.name||s.name; save(s); unlock(); }
      else { clear(); ready(showLogin); }
    }).catch(function(){ unlock(); });   /* offline or service down: keep a valid session working */
    return;
  }
  ready(showLogin);

  function ready(fn){ if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',fn); else fn(); }
  function showLogin(){
    if (document.getElementById('clGate')) return;
    var g=document.createElement('div'); g.id='clGate'; g.setAttribute('role','dialog'); g.setAttribute('aria-modal','true'); g.setAttribute('aria-labelledby','clTitle');
    g.innerHTML='<form class="cl-box" novalidate>'+
      '<div class="cl-brand">Capstone Property</div><h1 id="clTitle">Capstone Creatives</h1>'+
      '<div class="cl-step1"><p>Enter your WhatsApp number. We\u2019ll send you a 6-digit code.</p>'+
        '<div class="cl-row"><select aria-label="Country code"><option value="974">+974</option><option value="971">+971</option><option value="966">+966</option><option value="20">+20</option><option value="63">+63</option><option value="91">+91</option><option value="44">+44</option><option value="">Other</option></select>'+
        '<input class="cl-phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="WhatsApp number" aria-label="WhatsApp number"></div>'+
        '<button class="cl-go cl-send" type="submit">Send code on WhatsApp</button></div>'+
      '<div class="cl-step2" hidden><p class="cl-sentto"></p>'+
        '<input class="cl-code" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="••••••" aria-label="6-digit code">'+
        '<button class="cl-go cl-verify" type="submit">Verify</button><br>'+
        '<button class="cl-link cl-resend" type="button" disabled>Resend code</button> &nbsp; <button class="cl-link cl-change" type="button">Change number</button></div>'+
      '<div class="cl-msg" role="status" aria-live="polite"></div>'+
      '<div class="cl-foot">For Capstone Property team members only.</div></form>';
    document.body.appendChild(g);
    var f=g.querySelector('form'), cc=g.querySelector('select'), ph=g.querySelector('.cl-phone'), code=g.querySelector('.cl-code');
    var s1=g.querySelector('.cl-step1'), s2=g.querySelector('.cl-step2'), msg=g.querySelector('.cl-msg');
    var sendBtn=g.querySelector('.cl-send'), verBtn=g.querySelector('.cl-verify'), resend=g.querySelector('.cl-resend');
    var phone='', timer=0;
    var say=function(t){ msg.textContent=t||''; };
    ph.focus();
    function full(){ var d=ph.value.replace(/\D/g,''); if(d.indexOf('00')===0) d=d.slice(2); if(cc.value && d.indexOf(cc.value)!==0) d=cc.value+d.replace(/^0+/,''); return d; }
    function countdown(){ var t=60; resend.disabled=true; clearInterval(timer); resend.textContent='Resend code (60)';
      timer=setInterval(function(){ t--; resend.textContent='Resend code ('+t+')'; if(t<=0){ clearInterval(timer); resend.disabled=false; resend.textContent='Resend code'; } },1000); }
    function send(){ phone=full(); if(phone.length<10){ say('Please enter a valid WhatsApp number.'); return; }
      sendBtn.disabled=true; resend.disabled=true; say('Sending…');
      api({action:'request',phone:phone}).then(function(r){
        sendBtn.disabled=false;
        if(r&&r.ok){ s1.hidden=true; s2.hidden=false; g.querySelector('.cl-sentto').textContent='If +'+phone+' is registered, a code is on its way to WhatsApp. Enter it below.'; say(''); code.value=''; code.focus(); countdown(); }
        else say(r&&r.error==='too_many_requests'?'Too many codes requested. Please try again in an hour.':r&&r.error==='invalid_number'?'Please check the number.':'The code could not be sent. Please try again.');
      }).catch(function(){ sendBtn.disabled=false; say('No connection. Please try again.'); }); }
    function verify(){ var c=code.value.replace(/\D/g,''); if(c.length!==6){ say('Enter the 6-digit code.'); return; }
      verBtn.disabled=true; say('Checking…');
      api({action:'verify',phone:phone,code:c}).then(function(r){
        verBtn.disabled=false;
        if(r&&r.ok){ save({token:r.token,exp:r.exp,name:r.name,checked:Date.now()}); say(''); g.remove(); unlock(); }
        else { var e=r&&r.error; say(e==='wrong_code'?'That code is not right'+(r.left?' — '+r.left+' tries left.':'.'):e==='expired'?'The code expired. Tap Resend code.':e==='too_many_attempts'?'Too many tries. Tap Resend code.':'This number does not have access.'); code.select(); }
      }).catch(function(){ verBtn.disabled=false; say('No connection. Please try again.'); }); }
    f.addEventListener('submit',function(e){ e.preventDefault(); if(!s1.hidden) send(); else verify(); });
    code.addEventListener('input',function(){ code.value=code.value.replace(/\D/g,'').slice(0,6); if(code.value.length===6) verify(); });
    resend.addEventListener('click',send);
    g.querySelector('.cl-change').addEventListener('click',function(){ s2.hidden=true; s1.hidden=false; say(''); ph.focus(); });
  }
})();
