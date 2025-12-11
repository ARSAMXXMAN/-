import streamlit as st
from streamlit.components.v1 import html

# عنوان صفحه
st.set_page_config(page_title="کارت ویزیت", layout="centered")

# داده‌های کارت ویزیت
data = {
    "logoText": "GH",
    "fullName": "گلاره هوشمندیان",
    "jobTitle": "مدرس زبان انگلیسی، IELTS، و دورهٔ تربیت مدرس در تمامی سطوح و سنین",
    "phone": "+989125768056",
    "email": "Gelarehhm92@gmail.com",
}

# HTML و CSS کارت ویزیت
card_html = f"""
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:center;font-family:'Vazirmatn',sans-serif;margin-top:30px">

  <!-- کارت تیره -->
  <div style="width:350px;height:200px;border-radius:14px;overflow:hidden;position:relative;
              box-shadow:0 10px 30px rgba(2,6,23,0.6);
              background:linear-gradient(135deg,#ffc0cb,#071021);
              color:white;padding:18px;display:flex;flex-direction:column;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:12px">
      <div style="width:64px;height:64px;border-radius:10px;background:linear-gradient(135deg,#ff69b4,#7c3aed);
                  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;color:white;
                  box-shadow:0 6px 18px rgba(6,11,28,0.6)">
        {data["logoText"]}
      </div>
      <div>
        <h2 style="margin:0">{data["fullName"]}</h2>
        <p style="margin:0;font-size:13px;color:rgba(255,168,232,0.9)">{data["jobTitle"]}</p>
      </div>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:10px">
      <div style="display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:10px;background:rgba(255,255,255,0.03);font-size:13px">
        📞 {data["phone"]}
      </div>
      <div style="display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:10px;background:rgba(255,255,255,0.03);font-size:13px">
        📧 {data["email"]}
      </div>
    </div>
    <div style="margin-top:auto;display:flex;justify-content:flex-end">
      <div style="background:linear-gradient(90deg,#ff69b4,#7c3aed);padding:8px 12px;border-radius:10px;font-weight:600;color:#021023">
        Contact
      </div>
    </div>
  </div>

  <!-- کارت سفید -->
  <div style="width:350px;height:200px;border-radius:10px;background:white;color:#111827;padding:18px;display:flex;flex-direction:column;justify-content:space-between">
    <div style="display:flex;gap:12px;align-items:center">
      <div style="width:64px;height:64px;border-radius:10px;background:linear-gradient(90deg,#e2e8f0,#c7d2fe);
                  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;color:#111827">
        {data["logoText"]}
      </div>
      <div>
        <h2 style="margin:0;font-size:18px">{data["fullName"]}</h2>
        <p style="color:#475569;font-size:13px">{data["jobTitle"]}</p>
      </div>
    </div>
    <div style="font-size:13px;color:#374151;margin-top:auto">
      <div><strong>تلفن:</strong> {data["phone"]}</div>
      <div><strong>ایمیل:</strong> {data["email"]}</div>
    </div>
  </div>

</div>
"""

# نمایش HTML در Streamlit
html(card_html, height=300)