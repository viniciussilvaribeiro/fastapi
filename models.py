from pydantic import BaseModel

class Simulacao(BaseModel):
    valor_ref: int | None = None
    quantidade: int | None = None
    desconto: int | None = None
    valor_desc: int | None = None 
    bonus: int | None = None
    milhas_bonus: int | None = None
    valor_a_pagar: int | None = None
    milhas_receber: int | None = None
    valor_real_por_milheiro: int | None = None

    def cacular_valores(self):
        self.valor_desc = self.valor_ref - self.valor_ref / 100 * self.desconto
        self.milhas_bonus =  self.quantidade / 100 * self.bonus
        self.valor_a_pagar = self.valor_desc * (self.quantidade // 1000)
        self.milhas_receber = self.quantidade + self.milhas_bonus
        self.valor_real_por_milheiro = self.valor_a_pagar / (self.milhas_receber // 1000)