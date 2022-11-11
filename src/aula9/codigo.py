from conta import Conta, Cliente

cliente1 = Cliente('Clayton','Pereira','222222-32')
cliente2 = Cliente('Maiara','Souza','333333-11')

conta1 = Conta('123-1',cliente1, 180.0)
conta2 = Conta('123-2',cliente2, 220.0)

conta1.deposita(500)
conta1.saca(50)
conta1.transfere_para(conta2,130.0)
conta1.extrato()
conta2.extrato()

conta2.transfere_para(conta1,1000)
conta1.extrato()
conta2.extrato()

conta1.historico.imprime()