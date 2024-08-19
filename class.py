import pandas as pd
import pymysql
import matplotlib.pyplot as plt

class Configuracion_bd:
    # Configura la conexión a tu base de datos
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="tu_contraseña",
            database="companyData"
        )

    def cerrar_conexion(self):
        self.conn.close()

class leer_datos(Configuracion_bd):
    def __init__(self):
        super().__init__()
        # Consulta SQL para extraer los datos de la tabla
        self.query = "SELECT * FROM EmployeePerformance"
        self.df = None

    def ejecutar_consulta(self):
        self.df = pd.read_sql(self.query, self.conn)

    def procesar_datos(self):
        self.df['employee_id'] = pd.to_numeric(self.df['employee_id'], errors='coerce')
        self.df['performance_score'] = pd.to_numeric(self.df['performance_score'], errors='coerce')
        self.df['years_with_company'] = pd.to_numeric(self.df['years_with_company'], errors='coerce')
        self.df['salary'] = pd.to_numeric(self.df['salary'], errors='coerce')

        # Seleccionar solo las columnas relevantes
        self.df = self.df[['id', 'employee_id', 'department', 'performance_score', 'years_with_company', 'salary']]

    def mostrar_datos(self):
        print(self.df.head())
    
    def calcular_e_imprimir(self):
        # Calcular moda, mediana y desviación estándar de performance_score
        performance_mode = self.df['performance_score'].mode()[0] if not  self.df['performance_score'].mode().empty else None
        performance_median =  self.df['performance_score'].median()
        performance_std =  self.df['performance_score'].std()

        print("\nEstadísticas de performance_score:")
        print(f"Moda: {performance_mode}")
        print(f"Mediana: {performance_median}")
        print(f"Desviación Estándar: {performance_std}")

        # Calcular moda, mediana y desviación estándar de salary
        salary_mode =  self.df['salary'].mode()[0] if not  self.df['salary'].mode().empty else None
        salary_median =  self.df['salary'].median()
        salary_std =  self.df['salary'].std()

        print("\nEstadísticas de salary:")
        print(f"Moda: {salary_mode}")
        print(f"Mediana: {salary_median}")
        print(f"Desviación Estándar: {salary_std}")

        # Total de empleados por departamento
        total_employees_by_dept =  self.df['department'].value_counts()

        # Mostrar el total de empleados por departamento
        print("\nTotal de empleados por departamento:")
        print(total_employees_by_dept)

        # Calcular correlaciones
        correlation_years_performance =  self.df[['years_with_company', 'performance_score']].corr().iloc[0, 1]
        correlation_salary_performance =  self.df[['salary', 'performance_score']].corr().iloc[0, 1]

        # Muestra las correlaciones
        print("\nCorrelación entre years_with_company y performance_score: ", correlation_years_performance)
        print("Correlación entre salary y performance_score: ", correlation_salary_performance)

    def visualizacion_datos(self):

            # Visualización de Datos
            # Histograma del performance_score para cada departamento
            departments = self.df['department'].unique()
            for dept in departments:
                plt.figure(figsize=(10, 6))
                self.df[self.df['department'] == dept]['performance_score'].hist(bins=10, edgecolor='black')
                plt.title(f'Histograma de performance_score para {dept}')
                plt.xlabel('Performance Score')
                plt.ylabel('Frecuencia')
                plt.grid(False)
                plt.show()

            # Gráfico de dispersión de years_with_company vs. performance_score
            plt.figure()
            plt.scatter(self.df['years_with_company'],self.df['performance_score'])
            plt.title('Gráfico de dispersión de years_with_company vs. performance_score')
            plt.xlabel('Years with Company')
            plt.ylabel('Performance Score')
            plt.show()

            # Gráfico de dispersión de salary vs. performance_score
            plt.figure()
            plt.scatter(self.df['salary'], self.df['performance_score'])
            plt.title('Gráfico de dispersión de salary vs. performance_score')
            plt.xlabel('Salary')
            plt.ylabel('Performance Score')
            plt.show()


# Creamos una instancia de la clase leer_datos
lector = leer_datos()

# Llamamos a los métodos de la instancia
lector.ejecutar_consulta()
lector.procesar_datos()
lector.mostrar_datos()
lector.cerrar_conexion()
lector.calcular_e_imprimir()
lector.visualizacion_datos()


