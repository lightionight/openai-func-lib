from function_CRUD import EmbeddingMemory
from convert_data import convertTextToVector
if __name__ == "__main__":
    insert_data = [
        {
            'name': 'GetUserWeather',
            'keyword':['天气', '热不热', '下雨', '多云', '晒不晒'],
            'url': 'https://raw.githubusercontent.com/lightionight/openai-func-lib/main/GetUserWeather.yaml'
        },
        {
            'name': 'GetUserLocation',
            'keyword':['天气', '位置', '在哪', '地方'],
            'url': 'https://raw.githubusercontent.com/lightionight/openai-func-lib/main/GetUserLocation.yaml'
        },
        {
            'name': 'GetUserIP',
            'keyword':['IP', '地址', 'IP地址','网络地址'],
            'url': 'https://raw.githubusercontent.com/lightionight/openai-func-lib/main/GetUserIP.yaml'
        }
    ]
    insert_data2 = [
        {
            'name': 'v2ex_com',
            'keyword': ['v2ex', 'V2EX', 'v2ex最新消息', 'v2ex新闻'],
            'url': 'https://raw.githubusercontent.com/lightionight/openai-func-lib/main/v2ex_com.yaml'
        }
    ]
    function_lib =  EmbeddingMemory()
    #for item in insert_data2:
    #    vector_data = convertTextToVector(item['keyword'])
    #    print('inserting function: ', item['name'], '...')
    #    function_lib.insert( vector_data, item, 'test')
    #print('all function has insert successful')
    print('now test search is currect?')
    user_input = 'v2ex新闻'
    user_input_vector = convertTextToVector(user_input)
    response = function_lib.query(user_input_vector, 'test')
    print(response)
