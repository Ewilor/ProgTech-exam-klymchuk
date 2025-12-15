def calculate_pyramidal_sum(n):
    """
    Обчислює суму n трикутних чисел (тетраедричне число).
    Формула: n * (n + 1) * (n + 2) / 6
    """
    # Перевірка типу
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Вимога з завдання: при n < 0 генерувати виключення
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # Використовуємо цілочисельне ділення //
    result = (n * (n + 1) * (n + 2)) // 6
    return result