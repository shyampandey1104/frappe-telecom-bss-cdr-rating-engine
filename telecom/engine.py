"""Telecom BSS Call Detail Record (CDR) Rating & Postpaid Billing Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class CallDetailRecord:
    cdr_id: str
    msisdn: str
    call_type: str  # VOICE_LOCAL, VOICE_NATIONAL, DATA_MB, SMS
    duration_seconds: int
    data_volume_mb: float = 0.0
    is_roaming: bool = False


@dataclass
class RatedBillSummary:
    msisdn: str
    total_voice_duration_minutes: float
    total_data_gb: float
    total_voice_charges: float
    total_data_charges: float
    roaming_surcharges: float
    subtotal: float
    gst_18pct: float
    total_bill_amount: float


class TelecomRatingEngine:
    """High-throughput CDR rating matrix applying plan tariffs, roaming surcharges, and telecom taxes."""

    RATE_PER_VOICE_MINUTE = 0.60
    RATE_PER_MB_DATA = 0.05
    ROAMING_VOICE_SURCHARGE = 0.40

    def rate_cdrs_for_subscriber(self, msisdn: str, cdrs: List[CallDetailRecord]) -> RatedBillSummary:
        voice_seconds = 0
        data_mb_total = 0.0
        voice_charges = 0.0
        data_charges = 0.0
        roaming_charges = 0.0

        for c in cdrs:
            if c.call_type.startswith("VOICE"):
                voice_seconds += c.duration_seconds
                mins = c.duration_seconds / 60.0
                base = mins * self.RATE_PER_VOICE_MINUTE
                if c.is_roaming:
                    roam = mins * self.ROAMING_VOICE_SURCHARGE
                    roaming_charges += roam
                voice_charges += base
            elif c.call_type == "DATA_MB":
                data_mb_total += c.data_volume_mb
                data_charges += c.data_volume_mb * self.RATE_PER_MB_DATA

        subtotal = round(voice_charges + data_charges + roaming_charges, 2)
        gst = round((subtotal * 18.0) / 100.0, 2)
        total = round(subtotal + gst, 2)

        return RatedBillSummary(
            msisdn=msisdn,
            total_voice_duration_minutes=round(voice_seconds / 60.0, 2),
            total_data_gb=round(data_mb_total / 1024.0, 3),
            total_voice_charges=round(voice_charges, 2),
            total_data_charges=round(data_charges, 2),
            roaming_surcharges=round(roaming_charges, 2),
            subtotal=subtotal,
            gst_18pct=gst,
            total_bill_amount=total
        )
