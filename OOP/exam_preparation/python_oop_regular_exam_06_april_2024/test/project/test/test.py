from unittest import TestCase, main

from OOP.exam_preparation.python_oop_regular_exam_06_april_2024.test.project.social_media import SocialMedia


class SocialMediaTests(TestCase):
    allowed_platforms = ['Instagram', 'YouTube', 'Twitter']

    def setUp(self):
        self.media = SocialMedia(
            'test',
            'Instagram',
            100,
            'entertainment'
        )

    def test_correct_init(self):
        self.assertEqual(self.media._username, 'test')
        self.assertEqual(self.media._platform, 'Instagram')
        self.assertEqual(self.media._followers, 100)
        self.assertEqual(self.media._content_type, 'entertainment')
        self.assertEqual(self.media._posts, [])

    def test_platform_is_from_not_allowed_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.media.platform = 'Facebook'

        self.assertEqual(
            str(ve.exception),
            f"Platform should be one of {self.allowed_platforms}"
        )

    def test_create_post_and_upload_it(self):
        self.assertEqual(len(self.media._posts), 0)

        post_content = 'some content'
        self.media.create_post(post_content)

        self.assertEqual(len(self.media._posts), 1)

        expected_post = {
            'content': post_content,
            'likes': 0,
            'comments': []
        }

        self.assertEqual(self.media._posts[0], expected_post)
        self.assertEqual(
            self.media.create_post(post_content),
            f"New {self.media._content_type} post created by "
            f"{self.media._username} on {self.media._platform}."
        )



if __name__ == '__main__':
    main()