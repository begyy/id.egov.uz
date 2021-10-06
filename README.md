<p align="center">
  <img src="https://i.ibb.co/pzc3WjR/image.png"/>
</p>

```python
from one_id import OneID

one_id = OneID(username='my_username', password='my_password')
user = one_id.get_user('code', 'https://my_domain.com/?login=one_id')
if 'error' in user:
    print(user)
print(user)
```