import unittest
from main import extract, get_boundary_coordinates, get_data_and_description
from News  import News

class TestYourCode(unittest.TestCase):

    def test_extract(self):
        # Create some sample News objects for testing
        news_list = [
            News("News 1", "https://royanews.tv/news/300763", "roya", "2023-05-26T13:50:34+03:00"),
            # News("News 2", "id2", "roya", "2022-01-02")
        ]

        # Call the extract function
        extract(news_list)

        # Assert the expected results based on the provided code
        self.assertEqual(news_list[0].get_description(), "تسبب الزلزال في هزّة شدتها بنايات كبيرة في العاصمة لا يوجد خطر حدوث تسونامي جراء الزلزال وقع زلزال بلغت قوته 6.2 درجة قبالة سواحل طوكيو مساء الجمعة، مما أثار حالة من الهلع في المنطقة. أعلنت وكالة الأرصاد اليابانية أن مركز الزلزال كان على عمق 50 كيلومتراً. وحدث الزلزال في الساعة 19:03 بالتوقيت المحلي (10:03 ت غ) في مياه المحيط الهادئ قبالة منطقة تشيبا اليابانية. تسبب الزلزال في هزّة شدتها بنايات كبيرة في العاصمة وتسبب في توقف خدمات القطارات. وبالرغم من شدة الزلزال، أعلنت الوكالة اليابانية أنه لا يوجد خطر حدوث تسونامي جراء الزلزال. وتعمل السلطات اليابانية على تقييم الأضرار والتأكد من سلامة المواطنين. يذكر أن اليابان تعتبر منطقة نشطة زلزالياً وتتخذ تدابير وقائية مشددة للتعامل مع هذه الظواهر الطبيعية المدمرة.")
        # self.assertEqual(news_list[1].get_description(), "<expected description for roya news>")

    def test_get_boundary_coordinates(self):
        # Test case 1: Provide a valid place name
        place_name = "عمان"
        expected_coordinates = [(26.4361001, 52.0000019), (26.4361001, 60.30399999999999), (16.4571999, 60.30399999999999), (16.4571999, 52.0000019)]
        coordinates = get_boundary_coordinates(place_name)
        self.assertEqual(coordinates, expected_coordinates)
        place_name = "الجبيهة"
        expected_coordinates = [(32.0516517, 35.8518092), (32.0516517, 35.937103), (31.9857013, 35.937103), (31.9857013, 35.8518092)]
        coordinates = get_boundary_coordinates(place_name)
        self.assertEqual(coordinates, expected_coordinates)

        # Test case 2: Provide an empty place name
        place_name = ""
        expected_coordinates = None
        coordinates = get_boundary_coordinates(place_name)
        self.assertEqual(coordinates, expected_coordinates)

        # Add more test cases based on different scenarios

    def test_get_data_and_description(self):
        artical ="أعلنت وزارة الخارجية وشؤون المغتربين، الجمعة، تعرض منزل السفير الأردني في الخرطوم للاعتداء والتخريب."
        response = get_data_and_description(artical)
        for item in response:
            if isinstance(item, dict) and 'entity_group' in item:
                if item['entity_group'] == 'LOCATION':
                    self.assertEqual(item['word'], "الخرطوم")
    # Write test cases for the get_data_and_description function

if __name__ == '__main__':
    unittest.main()
