
import unittest

from main import classify_intent


class TestClassifyIntent(unittest.TestCase):

    def test_frame_intent(self):
        self.assertEqual(
            classify_intent("What is visible in this frame?"),
            "frame",
        )

    def test_whole_video_intent(self):
        self.assertEqual(
            classify_intent("Summarize the entire video"),
            "whole_video",
        )

    def test_clip_intent(self):
        self.assertEqual(
            classify_intent("When does the person enter the room?"),
            "clip",
        )

    def test_empty_question(self):
        with self.assertRaises(ValueError):
            classify_intent("")


if __name__ == "__main__":
    unittest.main()
