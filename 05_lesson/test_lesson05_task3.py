from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(
        By.TAG_NAME, "a")

    assert len(links) == 9, f"Найдено{len(links)} ссылок, а не 9"

    for i, link in enumerate(links, start=1):
        assert link.is_displayed(), f"Ссылка #{i} не видна"

    assert "1" in links[0].text, (
        f"В первой ссылке нет '1', а там '{links[0].text}'")

    print("Все проверки пройдены!")
    driver.quit()


if __name__ == "__main__":
    test_multiple_elements()
