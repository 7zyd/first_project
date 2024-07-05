from django.urls import reverse, resolve
from django.test import TestCase
from app01 import views
from app01.models import Board
from app01.views import board_topics


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)


class BoardTopicsTests(TestCase):

    # 假设您可能需要在这里设置一些测试前的条件，比如创建测试数据

    def test_board_topics_view_contains_navigation_links(self):
        # 使用reverse函数获取URL，确保pk参数正确设置
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')  # 主页URL
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})  # 新建话题URL

        # 发起GET请求到board_topics页面
        response = self.client.get(board_topics_url)

        # 检查响应中是否包含通往首页的链接
        self.assertContains(response, f'href="{homepage_url}"')

        # 检查响应中是否包含新建话题页面的链接
        self.assertContains(response, f'href="{new_topic_url}"')


