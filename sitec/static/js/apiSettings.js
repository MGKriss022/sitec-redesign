function api_v1(url){
    return '/api/v1/' + url
}

$.fn.api.settings.api = {
    'login': api_v1('accounts/login'),
    'logout': api_v1('accounts/logout'),
    'sync sitec': api_v1('sync-sitec'),
  }