class  Lavadora : 
    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar ()

    def _llenar_tanque (self, temperatura) :
            print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon (self):
            print('anadiendo jabon') 

    def _lavar(self):
        print ('Lavando la ropa')

    def _centrifugar(self):
        print ('centrifugando')



if __name__ == '__main__':
    Lavadora = Lavadora ()
    Lavadora.lavar()         
