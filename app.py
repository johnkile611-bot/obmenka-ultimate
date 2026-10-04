from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width'>
<style>body{margin:0;background:#0a0a0a;color:#fff;font-family:sans-serif;display:flex;justify-content:center;padding:15px}
.box{background:#1c1c1e;padding:22px;border-radius:28px;width:100%;max-width:360px;border:1px solid #333}
select,input{width:100%;background:#2c2c2e;color:#fff;border:none;padding:14px;border-radius:14px;margin-top:10px;font-size:16px}
.res{background:linear-gradient(135deg,#22c55e,#16a34a);padding:20px;border-radius:20px;text-align:center;margin-top:12px}
h1{font-size:36px;margin:5px 0}</style></head><body><div class=box><h2>💎 OBMENKA ULTIMATE</h2>
<select id='from' onchange='c()'><option value='10.9'>USD $</option><option value='1' selected>TJS</option><option value='11.8'>EUR</option><option value='0.113'>RUB</option><option value='0.00085'>UZS</option></select>
<input id='a' type='number' value='1000' oninput='c()'>
<div style='text-align:center'>🔄</div>
<select id='to' onchange='c()'><option value='10.9' selected>USD $</option><option value='1'>TJS</option><option value='11.8'>EUR</option><option value='0.113'>RUB</option></select>
<div class=res><div>NATIJА</div><h1 id='r'>0</h1></div>
</div><script>function c(){let f=parseFloat(document.getElementById('from').value),t=parseFloat(document.getElementById('to').value),a=parseFloat(document.getElementById('a').value)||0;document.getElementById('r').innerText=((a*f)/t).toFixed(2)}c()</script></body></html>
    """

if __name__=="__main__":
    app.run()
