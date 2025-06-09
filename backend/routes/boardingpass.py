from fastapi import APIRouter, Request
import pdfkit
import uuid
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/generate-pass")
async def generate_boarding_pass(request: Request):
    data = await request.json()
    name = data.get("name")
    flight = data.get("flight")
    terminal = data.get("terminal")
    counter = data.get("counter")
    qr_id = data.get("id")

    html = f"""
    <html>
    <head>
      <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        .card {{ border: 2px dashed #555; padding: 20px; width: 400px; }}
        .title {{ font-size: 24px; font-weight: bold; margin-bottom: 10px; }}
        .qr {{ margin-top: 20px; }}
      </style>
    </head>
    <body>
      <div class="card">
        <div class="title">Qatar Smart Travel - Boarding Pass</div>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Flight:</strong> {flight}</p>
        <p><strong>Terminal:</strong> {terminal}</p>
        <p><strong>Counter:</strong> {counter}</p>
        <div class="qr">
          <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={qr_id}" />
        </div>
      </div>
    </body>
    </html>
    """

    file_name = f"boarding_pass_{uuid.uuid4().hex[:6]}.pdf"
    path = f"./pdfs/{file_name}"
    pdfkit.from_string(html, path)

    return FileResponse(path, media_type="application/pdf", filename=file_name)
