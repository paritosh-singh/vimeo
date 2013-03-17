from . import BaseParser

# VimeoUser get vimeo user and
# parser it to make local user object
class VimeoUser(BaseParser):

    def __init__(self, id):
        if not isinstance(id, int):
            raise TypeError("`id` must be an integer.")
        params = dict(user_id=id)
        self.get(params)
        self.data = self.raw_data.get('person', {})
        if self.invalid_user(id): self.data = {}

    @property
    def id(self):
        id = self.data.get("id", None)
        return int(id) if id else None

    @property
    def username(self):
        return self.data.get("username", "")

    @property
    def display_name(self):
        return self.data.get("display_name", "")

    @property
    def is_staff(self):
        result = self.data.get("is_staff", 0)
        result = int(result)
        return True if result == 1 else False

    @property
    def has_uploaded(self):
        result = self.data.get("number_of_uploads", 0)
        result = int(result)
        return True if result > 0 else False

    @property
    def is_paying(self):
        is_plus = self.data.get("is_plus", 0)
        is_plus = int(is_plus)
        is_plus = True if is_plus == 1 else False
        is_pro = self.data.get("is_pro", 0)
        is_pro = int(is_pro)
        is_pro = True if is_pro == 1 else False
        return is_plus or is_pro

    @property
    def vimeo_url(self):
        return self.data.get("profileurl", "")


    @property
    def blank_user(self):
        return len(self.data.keys()) == 0

    # Get vimeo users with given params
    def get(self, params):
        if not isinstance(params, dict) and "user_id" not in params.keys():
            raise TypeError("Params not given in specified format or type.")
        params.update(method=u'vimeo.people.getInfo')
        super(VimeoUser, self).get(params)



    def invalid_user(self, id):
        return self.blank_user or self.id != id

# VimeoUsers do operation for collection of Vimeo users
class VimeoUsers(BaseParser):

    def __init__(self, users):
        if not isinstance(users, list):
            raise TypeError("`users` list must be an list object.")
        for user in users:
            if not isinstance(user, VimeoUser):
                raise TypeError("`user` in list must be a VimeoUser object.")
        self.collection = users

    def __repr__(self):
        values = [ repr(user) for user in self.collection ]
        return 'VimeoUsers' + str(values)

    def __getitem__(self, index):
        return self.collection[index]

    def append(self, user):
        if not isinstance(user, VimeoUser):
            raise TypeError("`user` in list must be a VimeoUser object.")
        self.collection.append(user)

    # Get required user ids specified in limit
    def get_required_user_ids(self, limit):
        self.user_ids = []
        count = 0
        params = dict(method = u"vimeo.categories.getAll", page=1,per_page=50)
        self.get(params)
        categories= self.raw_data['categories']
        if categories['total'] > 0:
            categories = categories['category']
            for category in categories:
                name = category.get('word')
                pages = 20
                for page in range(1,pages+1):
                    params = dict(method = u"vimeo.categories.getRelatedPeople", category=name, page=page,per_page=50)
                    self.get(params)
                    content = self.raw_data
                    pages = int(content['users']['total'])/50
                    if page > pages: break
                    users = content['users']['user']
                    for user in users:
                        if count >= limit: return None
                        user_id = int(user['id'])
                        if user_id not in self.user_ids:
                            self.user_ids.append(user_id)
                            count = count + 1

    @property
    def users(self):
        return self.collection

    @property
    def count(self):
        return len(self.users)