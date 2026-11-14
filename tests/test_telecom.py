import unittest
from telecom.engine import TelecomRatingEngine, CallDetailRecord

class TestTelecomRating(unittest.TestCase):
    def test_cdr_rating_aggregation(self):
        engine = TelecomRatingEngine()
        cdrs = [
            CallDetailRecord(
                cdr_id="CDR-01",
                msisdn="+91-9820011223",
                call_type="VOICE_LOCAL",
                duration_seconds=300 # 5 minutes
            ),
            CallDetailRecord(
                cdr_id="CDR-02",
                msisdn="+91-9820011223",
                call_type="VOICE_NATIONAL",
                duration_seconds=600, # 10 minutes roaming
                is_roaming=True
            ),
            CallDetailRecord(
                cdr_id="CDR-03",
                msisdn="+91-9820011223",
                call_type="DATA_MB",
                duration_seconds=0,
                data_volume_mb=500.0 # 500 MB
            )
        ]

        bill = engine.rate_cdrs_for_subscriber("+91-9820011223", cdrs)
        self.assertEqual(bill.total_voice_duration_minutes, 15.0)
        # Voice = 15 * 0.60 = 9.0
        self.assertEqual(bill.total_voice_charges, 9.0)
        # Roaming = 10 * 0.40 = 4.0
        self.assertEqual(bill.roaming_surcharges, 4.0)
        # Data = 500 * 0.05 = 25.0
        self.assertEqual(bill.total_data_charges, 25.0)
        # Subtotal = 9 + 4 + 25 = 38.0
        self.assertEqual(bill.subtotal, 38.0)
        # GST 18% = 6.84, Total = 44.84
        self.assertEqual(bill.total_bill_amount, 44.84)

if __name__ == "__main__":
    unittest.main()
