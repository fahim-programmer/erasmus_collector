
'''
Welcome to bot_lib_v3 and this a new project file
you can start by editing this script. Please run 
python bot_lib_v3 setup to install the required 
libraries.

'''

from bot_lib_v3 import Selenium_bot, Chrome_Driver, Excel

_path_dyn_each_program = '''//span[contains(text(),"Erasmus Mundus Catalogue")]//parent::h2//parent::div//parent::div//article'''
_path_com_program_title = f'''{_path_dyn_each_program}//h1//a'''
_path_com_program_abbr = f'''{_path_dyn_each_program}//p'''
_path_com_program_link = f'''{_path_dyn_each_program}//p//a'''
_path_com_program_locations = f'''{_path_dyn_each_program}//dd//div'''
_path_dyn_btn_next = '''//span[contains(text(),'Next')]//parent::a'''
_path_dyn_btn_previous = '''//span[contains(text(),'Previous')]//parent::a'''

Program = {
    'title':'program_title',
    'abbr':'SEMDA',
    'link':'https//www.programsite.com',
    'locations':'Spain, Belgium, Germany'
}

class main(Selenium_bot):
    def __init__(self):
        super().__init__(browser='Chrome', driver_exe=Chrome_Driver())
        #self.get_url('https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en')
        #data = self.extract()
        #self.object_dump(data, 'data_stash.pyobj')
        data = self.load_object('data_stash.pyobj')
        self.initalize_date_store(data)
        #self.timeout(10)
    
    def initalize_date_store(self, site_data):
        file = Excel.create("erasmus_latest_programs.xlsx")
        ws = file.active
        for index_p, each_program in enumerate(site_data):
            for index_d, each_param in enumerate(each_program):
                ws.cell(row=index_p + 1, column=index_d + 2, value=each_param)
        file.save("erasmus_latest_programs.xlsx")
    
    def extract(self):
        self.site_data = []
        while self.if_exists(_path_dyn_btn_next) is True:
            self.range_delay(2, 4)
            print(self.site_data)
            for each in range(0, 20):
                try:
                    program_title = self.elements_by_xpath(_path_com_program_title)[each].text
                    program_abbr = self.elements_by_xpath(_path_com_program_abbr)[each].text
                    program_link = self.elements_by_xpath(_path_com_program_link)[each].text
                    program_location = self.elements_by_xpath(_path_com_program_locations)[each].text
                    self.site_data.append([program_title, program_abbr, program_link, program_location])
                except Exception:
                    pass
            self.element_by_xpath(_path_dyn_btn_next, 1, 1).click()
        return self.site_data

if __name__ == '__main__':
    main()