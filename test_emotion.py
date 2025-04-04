import unittest
from app.emotion_detector import detect_emotion

class TestEmotionDetector(unittest.TestCase):
    def test_success(self):
        result = detect_emotion("I am happy")
        self.assertEqual(result["status"], "success")

    def test_error(self):
        result = detect_emotion("")
        self.assertEqual(result["code"], 400)

if __name__ == "__main__":
    unittest.main()