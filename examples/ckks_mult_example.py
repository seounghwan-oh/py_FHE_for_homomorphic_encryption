"""Example of CKKS multiplication."""

from ckks.ckks_decryptor import CKKSDecryptor
from ckks.ckks_encoder import CKKSEncoder
from ckks.ckks_encryptor import CKKSEncryptor
from ckks.ckks_evaluator import CKKSEvaluator
from ckks.ckks_key_generator import CKKSKeyGenerator
from ckks.ckks_parameters import CKKSParameters

def main():

    poly_degree = 8
    ciph_modulus = 1 << 600
    big_modulus = 1 << 1200
    scaling_factor = 1 << 30
    params = CKKSParameters(poly_degree=poly_degree,
                            ciph_modulus=ciph_modulus,
                            big_modulus=big_modulus,
                            scaling_factor=scaling_factor)
    key_generator = CKKSKeyGenerator(params)
    public_key = key_generator.public_key
    secret_key = key_generator.secret_key
    relin_key = key_generator.relin_key
    encoder = CKKSEncoder(params)
    encryptor = CKKSEncryptor(params, public_key, secret_key)
    decryptor = CKKSDecryptor(params, secret_key)
    evaluator = CKKSEvaluator(params)

    # result comparison
    message1 = [11000, 1, 1, 1]
    message2 = [0.05, 1, 1, 1]
    message3 = [5, 1, 1, 1]

    plain1 = encoder.encode(message1, scaling_factor)
    plain2 = encoder.encode(message2, scaling_factor)
    plain3 = encoder.encode(message3, scaling_factor)
    ciph1 = encryptor.encrypt(plain1)
    ciph2 = encryptor.encrypt(plain2)

    ciph_prod1 = evaluator.multiply(ciph1, ciph1, relin_key)
    for _ in range(3):
        ciph_prod1 = evaluator.multiply(ciph_prod1, ciph1, relin_key)

    ciph_prod2 = evaluator.multiply(ciph2, ciph2, relin_key)
    for _ in range(2):
        ciph_prod2 = evaluator.multiply(ciph_prod2, ciph2, relin_key)

    ciph_prod = evaluator.multiply(ciph_prod1, ciph_prod2, relin_key)
    result = evaluator.multiply_plain(ciph_prod, plain3)

    decrypted_prod = decryptor.decrypt(result)
    decoded_prod = encoder.decode(decrypted_prod)

    print(decoded_prod)

    for i in range(len(message1)):
        A1 = message1[i]
        A5 = A1 ** 5
        B1 = message2[i]
        B4 = B1 ** 4

        origin_result = abs(complex(5 * A5 * B4, 0))
        ckks_result = abs(decoded_prod[i])
        result = abs(complex(0.0001, 0))

        if ((origin_result - ckks_result) / (origin_result)) < result:
            print("True")
        else:
            print("False")

if __name__ == '__main__':
    main()
