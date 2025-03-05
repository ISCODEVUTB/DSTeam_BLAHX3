import unittest
import os
from Gestion_Paquete.location import Location
from Gestion_Paquete.users import User
import bcrypt

class TestUser(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba. Inicializar datos para Location y User con los cuales se van a hacer las pruebas posteriormente"""
        self.location = Location(
            country = "Colombia",
            department = "Bolivar",
            city = "Cartagena de Indias",
            address1 = "Cra. 11 #39-21, San Diego",
            address2 = "La Serrezuela",
            zip_code = 130001
        )

        # Obtén la contraseña desde la variable de entorno (si no está definida, se usa una contraseña predeterminada)
        password = os.getenv("USER_PASSWORD", "default_password")
        self.user = User(
            surname = "Joe",
            last_name = "Doe",
            national_id = "1037186420",
            email = "joedoe@hotmail.com",
            address = self.location,
            password = "Gatito123*"
        )

    def test_user_init(self):
        """Verificar que los valores iniciales sean iguales a los asignados para la prueba"""
        # assertEqual(first value, second value, message) Compara valores y mensaje en caso de que no sean iguales
        self.assertEqual(
            self.user.name,
            "Joe",
            "El nombre no se inicializó correctamente."
        )
        self.assertEqual(
            self.user.last_name,
            "Doe",
            "El apellido no se inicializó correctamente."
        )
        self.assertEqual(
            self.user.national_id,
            "1037186420",
            "El ID nacional no se inicializó correctamente."
        )
        self.assertEqual(
            self.user.email,
            "joedoe@hotmail.com",
            "El correo electrónico no se inicializó correctamente."
        )
        self.assertEqual(
            self.user.address,
            self.location,
            "La dirección no se inicializó correctamente."
        )

    def test_password_hashpwd(self):
        """Verificar que el la función hashpwd cree un hash de la contraseña"""
        original_password = "Gatito123*".encode('utf-8')
        hashed_password = self.user.hashpwd(original_password)
        # Comprobar que la constraseña no sea igual al hash
        self.assertNotEqual(
            original_password,
            hashed_password,
            "La contraseña no debe ser igual al hash"
        )
        #Comprobar que el hash creado coincida con la contraseña actual
        self.assertTrue(
            bcrypt.checkpw(original_password, hashed_password),
            "El hash de la contraseña no coincide con la original."
        )

if __name__ == "__main__":
    unittest.main()
