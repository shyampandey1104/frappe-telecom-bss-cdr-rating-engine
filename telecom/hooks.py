# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "telecom"
app_title = "Frappe Telecom Bss Cdr Rating Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Telecom Bss Cdr Rating Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/telecom/css/telecom.bundle.css"
app_include_js = "/assets/telecom/js/telecom.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "telecom.engine.on_document_submit",
        "on_cancel": "telecom.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "telecom.engine.daily_scheduled_sync"
    ]
}
