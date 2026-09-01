from selenium import webdriver

user1_cookie = {
    "name": "SESSION",
    "value": "NDg4YjI2NTMtZGQwMS00NTZmLTlhMTgtZmUxZjgwZTQwMTU3",
    "domain": "gitflic.ru"
}
user2_cookie = {
    "name": "SESSION",
    "value": "NTU1ODAyMTItMmMyMS00ZTMyLTkyYWItZTc4N2QwMTEzZmFl",
    "domain": "gitflic.ru"
}


def test_session_storage_auth():
    driver = webdriver.Chrome()

# Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
# Установите cookie пользователя 1.
    driver.add_cookie(user1_cookie)
# Обновите страницу.
    driver.refresh()
# Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/alexejskripnikov")
# Сохраните текущий URL.
    url_user1 = driver.current_url
    print(f"URL пользлвателя 1: {url_user1}")
# Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()
# Установите cookie пользователя 2.
    driver.add_cookie(user2_cookie)

# Обновите страницу.
    driver.refresh()

# Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/user22222222")

# Сохраните текущий URL.
    url_user2 = driver.current_url
    print(f"URL пользлвателя 2: {url_user2}")

# Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2, f"Ошибка: URL одинаковый: {url_user1}"

    driver.quit()
