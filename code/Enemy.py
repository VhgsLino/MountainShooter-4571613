#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT  # Importando WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # Atributos específicos do Enemy3
        if self.name == 'Enemy3':
            self.vertical_direction = 1  # 1 para descer, -1 para subir
            self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade padrão
            self.max_speed = self.vertical_speed  # Velocidade máxima para controle

    def move(self):
        # Movimento padrão para todos os inimigos (horizontal)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Lógica específica para o Enemy3
        if self.name == 'Enemy3':
            # Movimento vertical (subindo ou descendo)
            if self.vertical_direction == 1:  # Descer
                self.vertical_speed = ENTITY_SPEED[self.name] * 2  # Velocidade de descida dobrada
            elif self.vertical_direction == -1:  # Subir
                self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade de subida normal

            new_centery = self.rect.centery + self.vertical_speed * self.vertical_direction

            # Impedir que o inimigo ultrapasse os limites da tela verticalmente
            if new_centery < 0:
                new_centery = 0  # Impede que ultrapasse o topo
                self.vertical_direction = 1  # Começa a descer

            elif new_centery > WIN_HEIGHT:
                new_centery = WIN_HEIGHT  # Impede que ultrapasse a parte inferior
                self.vertical_direction = -1  # Começa a subir

            # Atualiza a posição vertical
            self.rect.centery = new_centery

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))