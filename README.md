# Reconstruct RSA Private Key

This Python script reconstructs an RSA private key given the public modulus `n`, public exponent `e`, and the prime factors `p` and `q` of `n`. Once the private exponent `d` is calculated, it generates the complete RSA private key in PEM format.

It's intended for educational purposes, CTF (Capture The Flag) challenges, and cryptography research, where RSA keys may be intentionally weak or partially exposed.

## Features
- Accepts an RSA public key and factors `n` using SageMath
- Computes φ(n) and the modular inverse of `e`
- Reconstructs the full RSA private key
- Outputs the key in PEM format

## Requirements

- Python 3.x
- [pwntools](https://docs.pwntools.com/en/stable/)
- [pycryptodome](https://pycryptodome.readthedocs.io/)
- [SageMath](https://www.sagemath.org/)

Install dependencies (except SageMath):

```
pip install pycryptodome pwntools
```

> ⚠️ SageMath must be installed and accessible from the environment where this script runs.

## Usage

Update the `key` object in the script with your RSA public key, then run:

```
python3 reconstruct_rsa_private_key.py
```

You will see output like this:

```
[+] e: 65537
[+] n: 123456789...
[+] p: ...
[+] q: ...
[+] m: ...
[+] d: ...
[+] Listing private key:

-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
```

---

# Reconstruir Clave Privada RSA

Este script en Python reconstruye una clave privada RSA a partir del módulo público `n`, el exponente público `e`, y los factores primos `p` y `q` de `n`. Una vez que se calcula el exponente privado `d`, genera la clave privada completa en formato PEM.

Está pensado para fines educativos, retos de CTF (Capture The Flag) y análisis criptográfico, donde las claves RSA pueden ser débiles o parcialmente reveladas.

## Características
- Acepta una clave pública RSA y factoriza `n` usando SageMath
- Calcula φ(n) y el inverso modular de `e`
- Reconstruye la clave privada completa
- Exporta la clave en formato PEM

## Requisitos

- Python 3.x
- [pwntools](https://docs.pwntools.com/en/stable/)
- [pycryptodome](https://pycryptodome.readthedocs.io/)
- [SageMath](https://www.sagemath.org/)

Instalar dependencias (excepto SageMath):

```
pip install pycryptodome pwntools
```

> ⚠️ SageMath debe estar instalado y accesible desde el entorno donde se ejecuta el script.

## Uso

Edita el objeto `key` en el script con tu clave pública RSA, luego ejecuta:

```
python3 reconstruct_rsa_private_key.py
```

Verás una salida como esta:

```
[+] e: 65537
[+] n: 123456789...
[+] p: ...
[+] q: ...
[+] m: ...
[+] d: ...
[+] Listando la clave privada:

-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
```

---

💡 **Disclaimer:** This script is for educational and ethical use only. Do not use it against systems or keys you do not own or have explicit permission to test.
