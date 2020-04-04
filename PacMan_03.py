import pygame

pygame.init()

tela_x = 800
tela_y = 600

screen = pygame.display.set_mode((tela_x, tela_y), 0)
amarelo = (255, 255, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
velocidade = 1

# escrever o score

fonte = pygame.font.SysFont("arial", 50, True, False)


class Cenario:
    def __init__(self, tamanho, pac):

        self.pacman = pac
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 0, 0, 2, 1, 2, 0, 0, 0, 2, 1, 1, 1, 1, 2, 0, 0, 0, 2, 1, 2, 0, 0, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def pintar_coluna(self, tela, numero_coluna, coluna):
        for numero_linha, linha in enumerate(coluna):
            x = numero_linha * self.tamanho
            y = numero_coluna * self.tamanho
            cor = preto
            metade_tamanho = self.tamanho // 2

            if linha == 2:
                cor = azul

            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)

            if linha == 1:
                pygame.draw.circle(screen, amarelo, (x + metade_tamanho, y + metade_tamanho), self.tamanho // 10, 0)

    def pintar(self, tela):
        for numero_coluna, coluna in enumerate(self.matriz):
            self.pintar_coluna(tela, numero_coluna, coluna)

        self.escrever(screen)

    def calcular_regras(self):
        col = pacman.coluna_intencao
        lin = pacman.linha_intencao

        if 0 <= lin < 28 and 0 <= col < 29:
            if self.matriz[col][lin] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[col][lin] == 1:
                    self.pontos += 1
                    self.matriz[col][lin] = 0

    def escrever(self, tela):
        pontos_x = 30 * self.tamanho
        texto = f"Score: {self.pontos}"
        img_texto = fonte.render(texto, True, amarelo)
        tela.blit(img_texto, (pontos_x, 100))


class Pacman:

    def __init__(self, tamanho):
        self.centro_x = 300
        self.centro_y = 400
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.vel_x = 0
        self.vel_y = 0
        self.linha = 1
        self.coluna = 1
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def pintar_boca_aberta(self, tela):
        # desenho  do corpo
        pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

        # desenho da boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - int(self.raio / 2))
        labio_inferior = (self.centro_x + self.raio, self.centro_y + int(self.raio / 2))

        pontos_boca = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, preto, pontos_boca, 0)

        # desenho do olho
        olho_x = int(self.centro_x + self.raio / 5)
        olho_y = int(self.centro_y - self.raio / 2)
        raio_olho = int(self.raio / 7)

        pygame.draw.circle(tela, preto, (olho_x, olho_y), raio_olho, 0)

    def regras(self):
        self.linha_intencao = self.linha + self.vel_x
        self.coluna_intencao = self.coluna + self.vel_y
        self.centro_y = self.coluna * self.tamanho + self.raio
        self.centro_x = self.linha * self.tamanho + self.raio

    def retorna_vel_x(self):
        return self.vel_x

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = velocidade

                elif e.key == pygame.K_LEFT:
                    self.vel_x = -velocidade

                elif e.key == pygame.K_UP:
                    self.vel_y = -velocidade

                elif e.key == pygame.K_DOWN:
                    self.vel_y = velocidade

            elif e.type == pygame.KEYUP:

                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0

                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0

                elif e.key == pygame.K_UP:
                    self.vel_y = 0

                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def processar_eventos_mouse(self, eventos):

        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.linha = (mouse_x - self.centro_x) // delay
                self.coluna = (mouse_y - self.centro_y) // delay

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao


if __name__ == "__main__":

    size = 600 // 30
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)

    while True:
        # regras
        pacman.regras()
        cenario.calcular_regras()

        # pintar
        if pacman.retorna_vel_x() > 0 or pacman.retorna_vel_x() <= 0:
            screen.fill(preto)
            cenario.pintar(screen)
            pacman.pintar_boca_aberta(screen)
            pygame.display.update()
            pygame.time.delay(100)

        # captura os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

        pacman.processar_eventos(eventos)
        # pacman.processar_eventos_mouse(eventos)
