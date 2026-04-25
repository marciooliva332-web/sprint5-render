"""Modulo para verificar e listar numeros primos."""
import math


def is_prime(n: int) -> bool:
    """Verifica se um numero n e primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main() -> None:
    """Contem toda a logica principal."""
    primes = [str(i) for i in range(100) if is_prime(i)]
    print(" ".join(primes))


if __name__ == "__main__":
    main()
