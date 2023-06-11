from django.test import TestCase
from lists.models import Item

class HomePageTest(TestCase):
    '''тест домашней страницы'''
    
    def test_uses_home_template(self):
        '''тест: домашняя страница возвращает правельный html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        
    def test_redirect_after_POST(self):
        '''тест: переадресует после post-запроса'''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
        
    def test_only_saves_items_when_necessary(self):
        '''тест: сохраняет элементы, только когда нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
        
    def test_displays_all_list_item(self):
        '''тест: отображаются все элементы списка'''
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/')
        print(response.content)
        
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())
        
        
class ItemModelTest(TestCase):
    '''тест модели элемента списка'''
    
    def test_saving_and_retrieving_items(self):
        '''тест сохраниения и получения элементов списка'''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)
        
        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')