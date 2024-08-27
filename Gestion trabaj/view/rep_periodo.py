from controllers.Cdate_active import DateActive, ControllersDateActive
from controllers.Cdate_work import DateWork, ControllersDateWork
from controllers.Cemployee import ControllersEmployee
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


class ReportesRango:
    def __init__(self):   
        self.controller_dateactive=ControllersDateActive()
        self.rango_fecha=self.controller_dateactive.listar_date_active()  
        self.controller_date_range= ControllersDateWork()
        self.controller_name=ControllersEmployee()  
        pass 

    def list_rangofecha(self):
        data = []
        for date_r in self.rango_fecha:
            fecha_ini = date_r.date_ini.strftime('%Y-%m-%d')
            fecha_fin = date_r.dete_fin.strftime('%Y-%m-%d')
            
            objeto_rango = self.controller_date_range.listar_date_work_range(fecha_ini, fecha_fin)
            for obj in objeto_rango:
                nombre_trabajador = self.controller_name.get_trabajador_id(obj.employee_id)
                data.append({
                    'nombre': nombre_trabajador,
                    'date': obj.date,
                    'work': obj.work,
                    'salaries': obj.salaries
                })

        self.export_to_excel(data, fecha_ini, fecha_fin)

    def export_to_excel(self, data, fecha_ini, fecha_fin):
        # Crear un DataFrame a partir de los datos
        df = pd.DataFrame(data)

        # Obtener el rango de fechas
        start_date = datetime.strptime(fecha_ini, '%Y-%m-%d')
        end_date = datetime.strptime(fecha_fin, '%Y-%m-%d')
        date_range = pd.date_range(start=start_date, end=end_date)

        # Crear un DataFrame con las columnas necesarias
        columns = ['nombre', 'Salario', 'a cobrar'] + [date.strftime('%d') for date in date_range]
        result_df = pd.DataFrame(columns=columns)

        # Rellenar el DataFrame
        for name, group in df.groupby('nombre'):
            row = {'nombre': name, 'Salario': group['salaries'].iloc[0]}
            row.update({date.strftime('%d'): '' for date in date_range})
            for _, entry in group.iterrows():
                row[entry['date'].strftime('%d')] = entry['work']
            row['a cobrar'] = (group['work'] == 'X').sum() * group['salaries'].iloc[0]
            result_df = pd.concat([result_df, pd.DataFrame([row])], ignore_index=True)

        # Exportar a Excel
        report_date = datetime.now().strftime('%Y%m%d')
        file_name = f"salario_{report_date}.xlsx"
        result_df.to_excel(file_name, index=False)
        
        # Ajustar el ancho de las celdas
        self.adjust_column_width(file_name)
        print(f"Reporte exportado a {file_name}")
        
        
    def adjust_column_width(self, file_name):
        # Cargar el libro de Excel
        workbook = load_workbook(file_name)
        worksheet = workbook.active

        # Ajustar el ancho de las columnas
        for col in worksheet.columns:
            max_length = 0
            column = col[0].column_letter  # Obtener la letra de la columna
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column].width = adjusted_width

        # Guardar el libro de Excel con los ajustes
        workbook.save(file_name)




