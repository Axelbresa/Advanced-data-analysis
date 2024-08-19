# import pandas as pd
# import pymysql
# import matplotlib.pyplot as plt


# # Configura la conexión a tu base de datos
# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="tu_contraseña",
#     database="companyData"
# )

# # Consulta SQL para extraer los datos de la tabla
# query = "SELECT * FROM EmployeePerformance"

# # Usa pandas para ejecutar la consulta y cargar los datos en un DataFrame
# df = pd.read_sql(query, conn)

# # Cierra la conexión
# conn.close()

# # Convertir columnas a tipos de datos apropiados
# df['employee_id'] = pd.to_numeric(df['employee_id'], errors='coerce')
# df['performance_score'] = pd.to_numeric(df['performance_score'], errors='coerce')
# df['years_with_company'] = pd.to_numeric(df['years_with_company'], errors='coerce')
# df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# # Seleccionar solo las columnas relevantes
# df = df[['id', 'employee_id', 'department', 'performance_score', 'years_with_company', 'salary']]

# # Mostrar el DataFrame con las columnas especificadas
# print(df.head())

# # Calcular moda, mediana y desviación estándar de performance_score
# performance_mode = df['performance_score'].mode()[0] if not df['performance_score'].mode().empty else None
# performance_median = df['performance_score'].median()
# performance_std = df['performance_score'].std()

# print("\nEstadísticas de performance_score:")
# print(f"Moda: {performance_mode}")
# print(f"Mediana: {performance_median}")
# print(f"Desviación Estándar: {performance_std}")

# # Calcular moda, mediana y desviación estándar de salary
# salary_mode = df['salary'].mode()[0] if not df['salary'].mode().empty else None
# salary_median = df['salary'].median()
# salary_std = df['salary'].std()

# print("\nEstadísticas de salary:")
# print(f"Moda: {salary_mode}")
# print(f"Mediana: {salary_median}")
# print(f"Desviación Estándar: {salary_std}")

# # Total de empleados por departamento
# total_employees_by_dept = df['department'].value_counts()

# # Mostrar el total de empleados por departamento
# print("\nTotal de empleados por departamento:")
# print(total_employees_by_dept)

# # Calcular correlaciones
# correlation_years_performance = df[['years_with_company', 'performance_score']].corr().iloc[0, 1]
# correlation_salary_performance = df[['salary', 'performance_score']].corr().iloc[0, 1]

# # Muestra las correlaciones
# print("\nCorrelación entre years_with_company y performance_score: ", correlation_years_performance)
# print("Correlación entre salary y performance_score: ", correlation_salary_performance)

# # Visualización de Datos
# # Histograma del performance_score para cada departamento
# departments = df['department'].unique()
# for dept in departments:
#     plt.figure(figsize=(10, 6))
#     df[df['department'] == dept]['performance_score'].hist(bins=10, edgecolor='black')
#     plt.title(f'Histograma de performance_score para {dept}')
#     plt.xlabel('Performance Score')
#     plt.ylabel('Frecuencia')
#     plt.grid(False)
#     plt.show()

# # Gráfico de dispersión de years_with_company vs. performance_score
# plt.figure()
# plt.scatter(df['years_with_company'], df['performance_score'])
# plt.title('Gráfico de dispersión de years_with_company vs. performance_score')
# plt.xlabel('Years with Company')
# plt.ylabel('Performance Score')
# plt.show()

# # Gráfico de dispersión de salary vs. performance_score
# plt.figure()
# plt.scatter(df['salary'], df['performance_score'])
# plt.title('Gráfico de dispersión de salary vs. performance_score')
# plt.xlabel('Salary')
# plt.ylabel('Performance Score')
# plt.show()
