class EmptyOptionalFragment(Exception):
    def __init__(
        self, msg='Fragmento opcional deve ter um diagrama valido',
        *args, **kwargs
    ):
        super().__init__(msg, *args, **kwargs)


class MessageFormatException(Exception):
    def __init__(
        self,
        msg='Mensagem precisa possuir nome, probabilidade e lifelines de ' +
        'origem e destino',
        *args, **kwargs
    ):
        super().__init__(msg, *args, **kwargs)


class EmptyGuardConditionException(Exception):
    def __init__(
        self,
        msg='Diagrama de sequencia precisa possuir uma condicao de guarda',
        *args, **kwargs
    ):
        super().__init__(msg, *args, **kwargs)
