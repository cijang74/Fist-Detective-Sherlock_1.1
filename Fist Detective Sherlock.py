####################################################################
#################################################################### 초기 설정

import pygame, sys, random, time
from pygame.locals import *

pygame.init() #파이게임 초기화

#화면 크기 설정
screen_width = 1920 # 가로크기
screen_height = 1080 # 세로크기

#게임 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#게임이름
pygame.display.set_caption('Pyramid_Escape')

#FPS
clock = pygame.time.Clock()

#각종 이미지 불러오기
homescreen_image = pygame.image.load('images/homescreen.png').convert()

one_image = pygame.image.load('images/1.png').convert()
one_image.set_colorkey((0, 0, 0))
two_image = pygame.image.load('images/2.png').convert()
two_image.set_colorkey((0, 0, 0))
three_image = pygame.image.load('images/3.png').convert()
three_image.set_colorkey((0, 0, 0))

clearscreen_image = pygame.image.load('images/clear.png').convert()
howtoplay_image = pygame.image.load('images/How_to_play.png').convert()

start_image = pygame.image.load('images/start.png').convert()
start_rect = start_image.get_rect()

end_image = pygame.image.load('images/end.png').convert()
end_rect = end_image.get_rect()

replay_image = pygame.image.load('images/replay.png').convert()
replay_rect = replay_image.get_rect()

how_to_butten_image = pygame.image.load('images/how_to_butten.png').convert()
how_to_butten_rect = how_to_butten_image.get_rect()

badguy_image = pygame.image.load('images/E_missile.png').convert()
badguy_image.set_colorkey((255, 255, 255))

boss_small_missile = pygame.image.load('images/B_missile.png').convert()
boss_small_missile.set_colorkey((255, 255, 255))

boss_missile_image = pygame.image.load('images/boss_missile.png').convert()
boss_missile_image.set_colorkey((255, 255, 255))

enemy_image = pygame.image.load('images/vhxkq.png').convert()
enemy_image.set_colorkey((0, 0, 0))

boss_image = pygame.image.load('images/boss.png').convert()
boss_image.set_colorkey((255, 255, 255))

wall_normal = pygame.image.load('images/wall_normal.png').convert()
wall_broken = pygame.image.load('images/wall_broken.png').convert()
wall_broken.set_colorkey((255, 255, 255))

character_image = pygame.image.load('images/character_top.png').convert()
character_image.set_colorkey((255, 255, 255))
character_size = character_image.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character2_image = pygame.image.load('images/character_left.png').convert()
character2_image.set_colorkey((255, 255, 255))
character2_size = character_image.get_rect().size
character2_width = character_size[0]
character2_height = character_size[1]
last = character_image

character_attack_image = pygame.image.load('images/character_attack.png').convert()
character_attack_image.set_colorkey((0, 255, 0))
character_attack_size = character_image.get_rect().size
character_attack_width = character_size[0]
character_attack__height = character_size[1]

character2_attack_image = pygame.image.load('images/character2_attack.png').convert()
character2_attack_image.set_colorkey((0, 255, 0))
character2_attack_size = character_image.get_rect().size
character2_attack_width = character_size[0]
character2_attack__height = character_size[1]

character_image_walk_1 = pygame.image.load('images/character_walk_1.png').convert()
character_image_walk_1.set_colorkey((255, 255, 255))
character_image_walk_2 = pygame.image.load('images/character_walk_2.png').convert()
character_image_walk_2.set_colorkey((255, 255, 255))
character_image_walk_1R = pygame.image.load('images/character_walk_1R.png').convert()
character_image_walk_1R.set_colorkey((255, 255, 255))
character_image_walk_2R = pygame.image.load('images/character_walk_2R.png').convert()
character_image_walk_2R.set_colorkey((255, 255, 255))

theif_image = pygame.image.load('images/Enemy.png').convert()
theif_image.set_colorkey((255, 255, 255))
theif_size = theif_image.get_rect().size
theif_width = character_size[0]
theif__height = character_size[1]

theif_image2 = pygame.image.load('images/Enemy_left.png').convert()
theif_image2.set_colorkey((255, 255, 255))
theif2_size = theif_image.get_rect().size
theif2_width = character_size[0]
theif2__height = character_size[1]

theif_attack_image = pygame.image.load('images/Enemy_attack.png').convert()
theif_attack_image.set_colorkey((0, 255, 0))

theif_attack_image2 = pygame.image.load('images/Enemy2_attack.png').convert()
theif_attack_image2.set_colorkey((0, 255, 0))

missile_image = pygame.image.load('images/missile.png').convert()
missile_image.set_colorkey((255, 255, 255))

portal_image = pygame.image.load('images/test.png').convert()
portal_image.set_colorkey((255, 255, 255))
un_portal_image = pygame.image.load('images/un_act_portal.png').convert()
un_portal_image.set_colorkey((255, 255, 255))
boss_portal_image = pygame.image.load('images/boss_portal.png').convert()
boss_portal_image.set_colorkey((255, 255, 255))

textbox_image = pygame.image.load('images/conText.png').convert()

textbox_image2 = pygame.image.load('images/conText2.png').convert()

textbox_image3 = pygame.image.load('images/conText3.png').convert()

textbox_image4 = pygame.image.load('images/conText4.png').convert()

textboxs_guide1 = pygame.image.load('images/Text.png').convert()

textboxs_guide2 = pygame.image.load('images/Text2.png').convert()

textboxs_guide3 = pygame.image.load('images/Text3.png').convert()

treasure_image = pygame.image.load('images/tkdwk.png').convert()
treasure_image.set_colorkey((0, 0, 0))

cave_trash_image = pygame.image.load('images/cave_trash.png').convert()
cave_trash_image.set_colorkey((255, 255, 255))

cave_trash2_image = pygame.image.load('images/cave_trash2.png').convert()
cave_trash2_image.set_colorkey((255, 255, 255))

space_trash_image = pygame.image.load('images/space_trash.png').convert()
space_trash_image.set_colorkey((255, 255, 255))

space_trash2_image = pygame.image.load('images/space_trash2.png').convert()
space_trash2_image.set_colorkey((255, 255, 255))

stage_museum = pygame.image.load('images/museum.png').convert()
stage_museum_ring = pygame.image.load('images/museum_ring.png').convert()
stage_museum_no_ring = pygame.image.load('images/museum_no_ring.png').convert()
stage_cave = pygame.image.load('images/cave.png').convert()
stage_broken_museum = pygame.image.load('images/museum_broken.png').convert()
stage_space = pygame.image.load('images/space.png').convert()
clear_News = pygame.image.load('images/News.png').convert()
bad_News = pygame.image.load('images/bad_news.png').convert()
Main_Buttun = pygame.image.load('images/Main.png').convert()
Main_Buttun_rect = Main_Buttun.get_rect()

GAME_OVER = pygame.image.load('images/gameover.png').convert()

#폰트들 설정
font = pygame.font.Font(None, 15)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 50)

#변수들 초기화
stage = 0
stop = 0
rewards = 0
high_score = 0
mapcounter = 1 #스테이지가 계속 호출되는 것을 막기 위한 변수
last_trash_spawn_time = 0
ggg = 0
fff = 0
ddd = 0.9
missile_speed = 10 #캐릭터 샷스피드
e_missile_speed = 8 #포탑 샷스피드
fire_range = 50 #포탑 공격 사거리

#사운드 불러오기
shot_sound = pygame.mixer.Sound('sounds/shot.wav')
walk_sound = pygame.mixer.Sound('sounds/walk.wav')
treasure_sound = pygame.mixer.Sound('sounds/treasure.wav')
portal_sound = pygame.mixer.Sound('sounds/portal.wav')
Boss_music = pygame.mixer.Sound('sounds/boss_music.wav')
stage_music = pygame.mixer.Sound('sounds/stage_music.wav')
clear_sound = pygame.mixer.Sound('sounds/clear_sound.wav')

####################################################################
#################################################################### 클래스

class Character: #플레이어 클래스
    def __init__(self):
        self.x = 130
        self.y = screen_height - 300
        self.dx = 0
        self.dy = 0
        self.range = 0
        self.stop = 0.0
        self.isJump = 0
        self.v = 1 # 속도
        self.m = 1  # 질량
        self.lastInput = 0 #벽에 닿기 직전 사용자가 어떤 방향키를 누르고 벽에 닿았는지 좌우상하 순으로 1, 2, 3, 4로 저장
        self.canMove_L = True #추가
        self.canMove_R = True #추가
        self.canMove_U = True #추가
        self.canMove_D = True #추가

        self.attac_speed = 0.6 #캐릭터 공격 속도(작을 수록 빨라짐)
        self.character_speed = 5 #캐릭터 이동 속도(클 수록 빨라짐)
        self.damage = 0 #캐릭터 공격 추가 데미지(클 수록 강해짐)
        self.hp = 3 #캐릭터 체력

        self.last_time = time.time()
        self.punch_time = time.time()-5

    def respawn(self): #플레이어 리스폰 위치(오른쪽으로 이동했을 때)
        self.x = 130
        self.y = screen_height - 300
        self.range = 0

    def respawn2(self): #플레이어 리스폰 위치(우주 그림에서 나왔을 떄)
        self.x = 800
        self.y = screen_height - 300
        self.range = 0

    def move(self, walls): #플레이어 이동 함수 + 벽을 지나갈 수 없게 하는 함수
        self.character_rect = pygame.Rect(self.x+30, self.y, 70, 128) ##추가
        self.character_rect_L = pygame.Rect(self.x+2, self.y+7, 5, 25) #추가
        self.character_rect_T = pygame.Rect(self.x+7, self.y+2, 25, 5) #추가
        self.character_rect_B = pygame.Rect(self.x+7, self.y+32, 25, 5) #추가
        ##이 부분부터 판정 알고리즘 수정
        wallCount = 0
        for wallCount in range(len(walls)):
            if self.character_rect_R.colliderect(walls[wallCount].wall_rect) == True:
                self.canMove_R = False
                break
            else:
                self.canMove_R = True

        wallCount = 0
        for wallCount in range(len(walls)):
            if self.character_rect_L.colliderect(walls[wallCount].wall_rect) == True:
                self.canMove_L = False
                break
            else:
                self.canMove_L = True

        wallCount = 0
        for wallCount in range(len(walls)):
            if self.character_rect_T.colliderect(walls[wallCount].wall_rect) == True:
                self.canMove_U = False
                break
            else:
                self.canMove_U = True

        wallCount = 0
        for wallCount in range(len(walls)):
            if self.character_rect_B.colliderect(walls[wallCount].wall_rect) == True:
                self.canMove_D = False
                break
            else:
                self.canMove_D = True
                
        if len(walls) == 0: # 마지막 벽이 깨질 때 벽에 붙어 있으면 이후 위의 for문이 안돌아 다시 self.canMove를 True로 돌리는 코드가 없었음, 또 다른 버그 생길 수도 있음
            self.canMove_L = True
            self.canMove_R = True
            self.canMove_U = True
            self.canMove_D = True
        #여기까지 판단 알고리즘

        
        if pressed_keys[K_LEFT] and self.x > 0 and istext_on == False: #세번째 조건 바뀜
            self.character_rect_T = pygame.Rect(self.x+32, self.y+7, 5, 25) #추가
            self.character_rect_B = pygame.Rect(self.x+2, self.y+7, 5, 25) #추가
            self.character_rect_L = pygame.Rect(self.x+7, self.y+2, 25, 5) #추가
            self.character_rect_R = pygame.Rect(self.x+7, self.y+32, 25, 5) #추가, 이하 나머지 방향키도 추가
            self.range = 180

            self.x -= self.character_speed
            self.lastInput = 1

            if (time.time() - self.stop)>0.4:
                pygame.mixer.Sound.play(walk_sound)
                self.stop = time.time()
            
        if pressed_keys[K_RIGHT] and self.x < 1920 - 130 and istext_on == False:
            self.character_rect_B = pygame.Rect(self.x+32, self.y+7, 5, 25)
            self.character_rect_T = pygame.Rect(self.x+2, self.y+7, 5, 25)
            self.character_rect_R = pygame.Rect(self.x+7, self.y+2, 25, 5)
            self.character_rect_L = pygame.Rect(self.x+7, self.y+32, 25, 5)
            self.range = 0
            
            self.x += self.character_speed
            self.lastInput = 2

            if (time.time() - self.stop)>0.4:
                pygame.mixer.Sound.play(walk_sound)
                self.stop = time.time()

        if pressed_keys[K_x] and istext_on == False:
            self.character_rect_R = pygame.Rect(self.x+32, self.y+7, 5, 25)
            self.character_rect_L = pygame.Rect(self.x+2, self.y+7, 5, 25)
            self.character_rect_T = pygame.Rect(self.x+7, self.y+2, 25, 5)
            self.character_rect_B = pygame.Rect(self.x+7, self.y+32, 25, 5)

            if character.isJump == 2:
                character.jump(1)
                
            if character.isJump == 0:
                character.jump(1)
                
            elif character.isJump == 1:
                character.jump(2)
    
    def jump(self, j):
        self.isJump = j

    def update(self):
        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:

            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (0.5 * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(0.5 * self.m * (self.v * self.v))

            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.y -= round(F)

            # 속도 줄여줌
            if stage == 6:
                self.v -= 0.09
            
            else:
                self.v -= 0.2

            # 바닥에 닿았을때, 변수 리셋
            if self.y > screen_height - 300:
                self.y = screen_height - 300
                self.isJump = 0
                if stage == 6:
                    self.v = 6

                else: 
                    self.v = 7

    def draw(self): #그리기(각도에 따라 로테이션 해줌)
        global last
        

        if pressed_keys[K_z] and istext_on == False:
            if last == character_image or last == character_image_walk_1 or last == character_image_walk_2 or last == character_attack_image:
                screen.blit(character_attack_image, (self.x, self.y))
                last = character_attack_image

            if last == character2_image or last == character_image_walk_1R or last == character_image_walk_2R or last == character2_attack_image:
                screen.blit(character2_attack_image, (self.x, self.y))
                last = character2_attack_image
        
        elif pressed_keys[K_LEFT] and istext_on == False: #왼
            if not(pressed_keys[K_z]):
                if time.time() - self.last_time > 0.4:
                    last = character_image_walk_1R
                    if time.time() - self.last_time > 0.8:
                        self.last_time = time.time()
                else:
                    last = character_image_walk_2R
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            last = character2_image

        elif pressed_keys[K_RIGHT] and istext_on == False: #오
            if not(pressed_keys[K_z]):
                if time.time() - self.last_time > 0.4:
                    last = character_image_walk_1
                    if time.time() - self.last_time > 0.8:
                        self.last_time = time.time()
                else:
                    last = character_image_walk_2
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            last = character_image

            


        screen.blit(last, (self.x, self.y))
    
    def fire(self): #미사일 발사(총구의 방향에서 발사되게 조정해놓음)
        if self.range == 0:
            missiles.append(Missile(self.x + 84, self.y + 64, self.range))

        if self.range == 180:
            missiles.append(Missile(self.x + 24, self.y + 64, self.range))

class Theif:
    def __init__(self,t):
        if stage <= 1:
            self.x = 1500
            self.y = screen_height - 300
            self.hp = 9999
        if stage == 2:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 9999
        if stage == 3:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 10
        if stage == 6:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 10
        if stage == 7:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 10
        self.t = t

    def stage1_move(self):
        self.x += 18

    def stage2_move(self):
        self.y -= 18

    def stage3_move(self,x):
        self.x = x
        self.x += 18

    def draw(self):
        if self.t == "attack":
            screen.blit(theif_attack_image, (self.x, self.y))
        else:
            screen.blit(theif_image, (self.x, self.y))

    def draw2(self):
        if self.t == 'attack':
            screen.blit(theif_attack_image2, (self.x, self.y))
        else:
            screen.blit(theif_image2, (self.x, self.y))
    
    def hit(self, missiles): #도둑 피격 판정
        return self.y < missiles.y + 26 and missiles.y < self.y + 128 and self.x < missiles.x + 8 and missiles.x < self.x + 128

    def fire(self): #십자방향으로 포탑 총알 발사
        if character.x > self.x:
            badguys.append(Badguy_Left(self.x + 80, self.y + 40))
        else:
            badguys.append(Badguy_Right(self.x + 15, self.y + 40))

class Missile: # 미사일 클래스
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def move(self):
        if self.r == 0:
            self.x += missile_speed # 총알 샷스피드가 높을수록 미사일의 샷스피드가 빨라짐

        if self.r == 180:
            self.x -= missile_speed

    def off_screen(self): #총알이 화면을 벗어났을 때 없애주는 함수
        if (self.x < character.x - 50):
            return True
        if (self.x > character.x + 150):
            return True

    def draw(self):
        
        if self.r == 0:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

        if self.r == 180:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

        if self.r == 90:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

        if self.r == 270:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

class Cave_Trash:
    def __init__(self):
        self.x = random.randint(50, 1870)
        self.y = -100
        self.dy = random.randint(2, 6)
        self.rr = random.randint(1,2)

    def move(self):
        self.dy += 0.1
        self.y += self.dy # 배드가이의 움직임
             
    def draw(self):
        if self.rr == 1:
            screen.blit(cave_trash_image, (self.x, self.y)) # 그리기
        if self.rr == 2:
            screen.blit(cave_trash2_image, (self.x, self.y)) # 그리기

    def off_screen(self):
        return (self.y > 1200) # 화면을 넘어갔을 때

    def touching(self, missile):
        self.cave_trach_rect = pygame.Rect(self.x, self.y, 80, 200) ##추가
        return self.cave_trach_rect.colliderect(missile.character_rect)##추가

class Space_Trash:
    def __init__(self):
        self.x = 2000
        self.y =  random.randint(50, 1030)
        self.rr = random.randint(1,2)
        self.dx = random.choice((2, 6))

    def move(self):
        self.dx += 0.1
        self.x -= self.dx # 배드가이의 움직임
             
    def draw(self):
        if self.rr == 1:
            screen.blit(space_trash_image, (self.x, self.y)) # 그리기
        if self.rr == 2:
            screen.blit(space_trash2_image, (self.x, self.y)) # 그리기

    def off_screen(self):
        return (self.x < -200) # 화면을 넘어갔을 때

    def touching(self, missile):
        self.space_trach_rect = pygame.Rect(self.x, self.y, 80, 80) ##추가
        return self.space_trach_rect.colliderect(missile.character_rect)##추가

class TextBox:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def draw(self):
        if self.t == "one":
            screen.blit(textbox_image, (self.x, self.y))
        if self.t == "two":
            screen.blit(textbox_image2, (self.x, self.y))
        if self.t == "three":
            screen.blit(textbox_image3, (self.x, self.y))
        if self.t == "four":
            screen.blit(textbox_image4, (self.x, self.y))

class Wall: #벽 클래스
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = stage * 6
        self.wall_state = wall_normal #기본은 기본 벽 텍스처
        self.wall_rect = pygame.Rect(self.x, self.y, 40, 40) #벽 범위

    def draw(self):
        screen.blit(self.wall_state, (self.x, self.y))

    def hit(self, missiles): #벽 피격 판정(미사일: 10*32, 벽: 40*40)
        if missiles.r == 0:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 180:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 90:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40
        if missiles.r == 270:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40

class Enemy: #포탑 클래스
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = stage
        self.last_badguy_spawn_time = time.time() 

    def draw(self):
        screen.blit(enemy_image, (self.x, self.y))

    def hit(self, missiles): #벽 피격 판정(미사일: 10*32, 포탑: 40*40)
        if missiles.r == 0:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 180:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 90:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40
        if missiles.r == 270:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40

    def fire(self): #십자방향으로 포탑 총알 발사
        badguys.append(Badguy_Down(self.x + 8, self.y + 5))
        badguys.append(Badguy_Up(self.x + 8, self.y + 15))
        badguys.append(Badguy_Left(self.x + 5, self.y + 8))
        badguys.append(Badguy_Right(self.x + 15, self.y + 8))

class Boss: #보스 클래스
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100
        self.last_badguy_spawn_time = time.time()
        self.last_badguy_spawn_time2 = time.time()

    def hit(self, missiles): #보스 피격 판정(미사일: 10*32, 보스: 360*360)
        return self.y < missiles.y + 26 and missiles.y < self.y + 360 and self.x < missiles.x + 8 and missiles.x < self.x + 360

    def draw(self):
        screen.blit(boss_image, (self.x, self.y))
        
    def fire_big(self): #무작위 패턴의 미사일 큰거 3발 + 미사일 작은거 2발 발사
        randome_one = random.randint(1,5)
        randome_two = random.randint(1,5)

        if randome_one == 1 or randome_two == 1:
            boss_missiles.append(Boss_Down1(self.x - 260, self.y))
        if randome_one == 2 or randome_two == 2:
            boss_missiles.append(Boss_Down1(self.x + 40, self.y + 300))
        if randome_one == 3 or randome_two == 3:
            boss_missiles.append(Boss_Down1(self.x + 360, self.y))

    def fire_small(self):
        randome_three = random.randint(1,5)
        randome_four = random.randint(1,5)

        if randome_three == 1 or randome_four == 1:
            boss_missiles.append(Boss_small_Down1(self.x - 10, self.y + 300))
            boss_missiles.append(Boss_small_Down1(self.x + 330, self.y + 300))

        if randome_three == 2 or randome_four == 2:
            boss_missiles.append(Boss_small_Down1(self.x + 20, self.y + 300))
            boss_missiles.append(Boss_small_Down1(self.x + 300, self.y + 300))


class Boss_Down1: #보스 미사일 큰거
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y += e_missile_speed
             
    def draw(self):
        screen.blit(boss_missile_image, (self.x, self.y))

    def off_screen(self):
        if (self.y < -800):
            return True
        elif (self.y > 728):
            return True
        elif (self.x < -800):
            return True
        elif (self.x > 1288):
            return True

    def touching_c(self, caracter): #캐릭터와 충돌했을 떄
        return self.y + 40 < caracter.y + 40 and caracter.y < self.y + 180 and self.x + 40 < caracter.x + 30 and caracter.x < self.x + 220

class Boss_small_Down1: #보스 미사일 작은거
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y += e_missile_speed
             
    def draw(self):
        screen.blit(boss_small_missile, (self.x, self.y))

    def off_screen(self):
        if (self.y < -800):
            return True
        elif (self.y > 728):
            return True
        elif (self.x < -800):
            return True
        elif (self.x > 1288):
            return True

    def touching_c(self, caracter):
        return self.y < caracter.y + 40 and caracter.y < self.y + 25 and self.x - 10 < caracter.x + 30 and caracter.x < self.x + 35

class Badguy_Down: #포탑 미사일(아래 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y += e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles): #내 캐릭터의 미사일에 닿았을 때
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        return self.y < caracter.y + 40 and caracter.y < self.y + 25 and self.x < caracter.x + 30 and caracter.x < self.x + 25

class Badguy_Up: #포탑 미사일(위 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y -= e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles):
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        return self.y < caracter.y + 30 and caracter.y < self.y + 25 and self.x < caracter.x + 30 and caracter.x < self.x + 25

class Badguy_Left: #포탑 미사일(왼쪽 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.x += e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles):
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        self.badguy_L_rect = pygame.Rect(self.x, self.y, 45, 45) ##추가
        return self.badguy_L_rect.colliderect(caracter.character_rect)##추가

class Badguy_Right: #포탑 미사일(오른쪽 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.x -= e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles):
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        self.badguy_R_rect = pygame.Rect(self.x, self.y, 45, 45) ##추가
        return self.badguy_R_rect.colliderect(caracter.character_rect)##추가

class Treasure: #보물상자 클래스
    def __init__(self):
        self.x = 800
        self.y = 20
        self.act = False #기본으로 False

    def draw(self):
        screen.blit(treasure_image, (self.x, self.y))

    def touch(self): #포탈과 닿았을 때(캐릭터: 40*40, 상자: 40*40)
        return (self.y < character.y + 40 and character.y < self.y + 40 and self.x < character.x + 40 and character.x < self.x + 40)

    def reward(self, rewards): #보물상자 보상
        global rewards_text
        global missile_speed

        if rewards == 1:
            character.hp += 3
            rewards_text = font2.render('hp 3 recovery', True, (0,0,0))

        if rewards == 2:
            rewards_text = font2.render('attac speed up', True, (0,0,0))
            character.attac_speed -= 0.2

        if rewards == 3:
            rewards_text = font2.render('damage up', True, (0,0,0))
            character.damage += 2

        if rewards == 4:
            rewards_text = font2.render('shot speed up', True, (0,0,0))
            missile_speed += 10


class Stage: #스테이지 클래스
    def __init__(self):
        self.x = 0
        self.y = 0

    def homescreen(self): #게임 메인화면(시작화면)
        screen.blit(homescreen_image, (self.x, self.y))
        Button(start_image,610,820,313,97,start_image,610,820,'start')
        Button(end_image,1180,820,313,97,end_image,1180,820,'end')

    def clearscreen(self): #게임 클리어 화면
        screen.blit(clearscreen_image, (self.x, self.y))
        Button(replay_image,210,520,313,97,replay_image,210,520,'replay')
        Button(end_image,780,520,313,97,end_image,780,520,'end')

    #스테이지 편하게 말들기 위한 함수들
    def makeWall_garo(self, x, y, i):
        for z in range (0, i+1):   
            walls.append(Wall(x + 40 * z, y))

    def makeWall_sero(self, x, y, i):
        for z in range (0, i+1):   
            walls.append(Wall(x, y + 40 * z))

    #각 스테이지들에서의 오브젝트 배치

    def stage1(self):
        screen.blit(stage_museum, (0, 0))
        textboxs.append(TextBox(1400,620,"one"))
        textboxs.append(TextBox(30,620,"two"))

    def stage2(self):
        screen.blit(stage_museum_ring, (0, 0))

    def stage3(self):
        pass

    def stage4(self):
        pass
        
    def stage5(self):
        pass

    def stage6(self):
        pass     

    def stage7(self):
        textboxs.append(TextBox(1400,620,"three"))
        textboxs.append(TextBox(720,620,"four"))
    def stage8(self):
        pass

    def stage9(self):
        pass

    def stage10(self):
        pass

class Button: #버튼 클래스
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, type):
        mouse = pygame.mouse.get_pos()

        if type == 'start':
            start_rect.left = x
            start_rect.top = y

        elif type == 'end':
            end_rect.left = x
            end_rect.top = y

        elif type == 'replay':
            Main_Buttun_rect.left = x
            Main_Buttun_rect.top = y

        elif type == 'howto':
            how_to_butten_rect.left = x
            how_to_butten_rect.top = y

        if x + width > mouse[0] > x and y + height > mouse[1] > y: #이미지 위에 마우스를 올리면 이미지 좌표 바꿔주기
            screen.blit(img_act,(x_act, y_act))

        else:
            screen.blit(img_in,(x,y))

character = Character()
Map = Stage()
treasure = Treasure() #한번만 쓸것들
theif = Theif("")

badguys = []
enemys = []
walls = []
textboxs = []
boss = []
missiles = []
boss_missiles = [] #배열로 여러개 만들것들
cave_trashs = []
space_trashs = []
####################################################################
#################################################################### 게임루프

while 1:
    dt = clock.tick(60) #초당 프레임수는 60이다.
    pressed_keys = pygame.key.get_pressed() # 코딩 편하게 할려고 미리 써 놓은거 (게임과는 상관 X)

    for event in pygame.event.get():

        if event.type == QUIT:
            sys.exit() # X 누르면 나가기

        if event.type == KEYDOWN and event.key == K_z:
            if stage >= 1 and istext_on == False:
                character.fire() # SPACE 누르면 총알 발사
                pygame.mixer.Sound.play(shot_sound)

    #스테이지 설정들
    if stage == 0: #시작화면 스테이지 값: 0
        Map.homescreen()
        if pygame.mouse.get_pressed()[0] and start_rect.collidepoint(pygame.mouse.get_pos()):
            stage += 1
        elif pygame.mouse.get_pressed()[0] and end_rect.collidepoint(pygame.mouse.get_pos()):
            sys.exit()

    if stage == 11 and mapcounter == 11: #클리어 화면 스테이지 값: 11
            enemys.clear()
            badguys.clear()
            walls.clear()
            Map.clearscreen()

            score = (character.hp * 100) - (int(start_time - time.time())) #점수 계산
            if high_score < score:
                    high_score = score

            #점수 화면에 띄우기
            c_txt2 = font3.render(str(int(score)), True, (0, 0, 0))
            c_txt3 = font3.render('Score: ', True, (0, 0, 0))
            c_txt4 = font3.render(str(int(high_score)), True, (0, 0, 0))
            c_txt5 = font3.render('High Score: ', True, (0, 0, 0))

            screen.blit(c_txt2, (325, 400))
            screen.blit(c_txt3, (210, 400))
            screen.blit(c_txt4, (980, 400))
            screen.blit(c_txt5, (780, 400))

            #boss_music_loop.stop()
            pygame.mixer.Sound.play(clear_sound)
            mapcounter += 1
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit() # X누르면 나가기

                if pygame.mouse.get_pressed()[0] and Main_Buttun_rect.collidepoint(pygame.mouse.get_pos()):
                    last_fire = 0
                    stage = 0
                    score = 0
                    mapcounter = 1
                    missile_speed = 10
                    character = Character()
                    Map = Stage()
                    treasure = Treasure()
                    badguys = []
                    enemys = []
                    walls = []
                    boss = []
                    missiles = []
                    boss_missiles = []
                    Map.homescreen()
                    time.sleep(0.5)
                    break

                elif pygame.mouse.get_pressed()[0] and end_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
                    
                pygame.display.update() #화면에 나타내기
    
    if stage > 0:
        if stage == 1:
            screen.blit(stage_museum_no_ring, (0, 0))
            theif.draw()
        if stage == 2:
            screen.blit(stage_museum, (0, 0))
        if stage == 3:
            screen.blit(stage_cave, (0, 0))
        if stage == 4:
            screen.blit(stage_museum, (0, 0))
        if stage == 5:
            screen.blit(stage_broken_museum, (0, 0))
        if stage == 6:
            screen.blit(stage_space, (0, 0))
        if stage == 7:
            screen.blit(stage_broken_museum, (0, 0))
        if stage == 8:
            screen.blit(clear_News, (0, 0))
        
        character.move(walls)
        character.draw()
        character.update()

        if stage == 1 and mapcounter == 1:
            start_time = time.time()
            Map.stage1()
            theif.x = 1500
            theif.y = screen_height - 300
            treasure_txt = False
            mapcounter += 1
            
            stage_music_loop = pygame.mixer.Sound(stage_music)
            stage_music_loop.play(-1) #음악 반복 재생

        if stage == 2 and mapcounter == 2:
            Map.stage2()
            theif.x = 300
            theif.y = screen_height - 300
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 3 and mapcounter == 3:
            Map.stage3()
            theif.x = 1500
            theif.y = screen_height - 300
            theif.hp = 10
            mapcounter += 1
            character.hp += 1
            treasure.act = False #3배수 스테이지 마다 보물상자 출현
            treasure_txt = False

        if stage == 4 and mapcounter == 4:
            Map.stage4()
            theif.x = 300
            theif.y = screen_height - 300
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 5 and mapcounter == 5:
            Map.stage5()
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 6 and mapcounter == 6:
            Map.stage6()
            character.v = 6
            character.m = 1.8
            theif.x = 1500
            theif.y = screen_height - 300
            theif.hp = 10
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 7 and mapcounter == 7:
            Map.stage7()
            character.v = 1
            character.m = 1
            theif.x = 1500
            theif.y = screen_height - 300
            theif.hp = 10
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 8 and mapcounter == 8:
            Map.stage8()
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 9 and mapcounter == 9:
            Map.stage9()
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

        if stage == 10 and mapcounter == 10:
            Map.stage10()
            mapcounter += 1
            character.hp += 1
            treasure.act = False
            treasure_txt = False

            #stage_music_loop.stop() #보스전이 아닌 스테이지의 Bgm 끄기

            #boss_music_loop = pygame.mixer.Sound(Boss_music)
            #boss_music_loop.play(-1) #보스전 음악 반복재생

        #대화형 텍스트 박스 관련
        istext_on = False
        t = 0
        if stage == 1 and t < len(textboxs):
            textboxs[t].draw()
            istext_on = True
            if pressed_keys[K_z]:
                if (time.time() - stop) > character.attac_speed:
                    del textboxs[t]
                    stop = time.time()

        spawn = True
        if stage == 7 and t < len(textboxs):
            textboxs[t].draw()
            istext_on = True
            spawn = False
            if pressed_keys[K_z]:
                if (time.time() - stop) > character.attac_speed:
                    del textboxs[t]
                    stop = time.time()

        #스테이지 안내형 텍스트 박스 관련
        if stage == 2:
            if character.x < 350 and character.x > 200:
                screen.blit(textboxs_guide1, (170, 620))
                if pressed_keys[K_UP]:
                    stage = 3
                    character.respawn()

        if stage == 4:
            if character.x < 970 and character.x > 820:
                screen.blit(textboxs_guide2, (800, 620))

            if character.x < 1600 and character.x > 1450:
                screen.blit(textboxs_guide3, (1430, 620))
                if pressed_keys[K_z]:
                    stage = 5

        if stage == 5:
            if character.x < 970 and character.x > 820:
                screen.blit(textboxs_guide1, (800, 620))
                if pressed_keys[K_UP]:
                    stage = 6
                    character.respawn()
        
        # 도둑의 움직임과 관련된 함수
        if stage == 1 and theif.x < 1920:
            if len(textboxs) == 0:
                theif.stage1_move()
                theif.draw()

        if stage == 2 and theif.y > 350:
            theif.stage2_move()
            theif.draw()

        if stage == 3:
            if theif.x > character.x: #오른쪽 방향을 보게 해야함   
                theif.draw2()

            if theif.x < character.x: #왼쪽 방향을 보게 해야함
                theif.draw()
            
            if time.time() - last_trash_spawn_time> 0.4+ ggg and spawn == True: # 쓰레기들 스폰
                cave_trashs.append(Cave_Trash())
                ggg -= 0.002
                last_trash_spawn_time = time.time()

        if stage == 4 and theif.y > 350:
            theif.stage2_move()
            theif.draw()

        if stage == 6:
            if theif.x > character.x: #오른쪽 방향을 보게 해야함   
                theif.draw2()

            if theif.x < character.x: #왼쪽 방향을 보게 해야함
                theif.draw()

            if time.time() - last_trash_spawn_time > 1+ fff: # 쓰레기들 스폰
                space_trashs.append(Space_Trash())
                fff -= 0.002
                last_trash_spawn_time = time.time()

        if stage == 7:
            if theif.x > character.x: #오른쪽 방향을 보게 해야함   
                theif.draw2()

            if theif.x < character.x: #왼쪽 방향을 보게 해야함
                theif.draw()

        if stage == 3:
            cc = 0
            while cc < len(cave_trashs): #i가 현재 배드가이의 개체수 보다 작을 때 동안 반복
                cave_trashs[cc].move()# 움직임
                cave_trashs[cc].draw()# 그리기
    
                if cave_trashs[cc].off_screen(): #만약에 화면을 넘어가면
                    del cave_trashs[cc] # 배드가이 삭제
                    cc -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성
                elif cave_trashs[cc].touching(character):##추가
                    character.hp -= 1##추가
                    del cave_trashs[cc]##추가
                    cc -= 1##추가
                cc += 1

        if stage == 6:
            ss = 0
            while ss < len(space_trashs): #i가 현재 배드가이의 개체수 보다 작을 때 동안 반복
                space_trashs[ss].move()# 움직임
                space_trashs[ss].draw()# 그리기
                
                if space_trashs[ss].off_screen(): #만약에 화면을 넘어가면
                    del space_trashs[ss] # 배드가이 삭제
                    ss -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성
                elif space_trashs[ss].touching(character):##추가
                    character.hp -= 1##추가
                    del space_trashs[ss]##추가
                    ss -= 1##추가
                ss += 1

        #포탈 관련: 닿으면 캐릭터를 리스폰 위치로 옮기고 스테이지 1 증가
        if character.x > 1920 - 140 and (stage == 1 or ((stage == 3 or stage == 6) and theif.x >1920)): # 좌표 조건식으로 변경
            stage += 1
            if stage == 7:
                character.respawn2()
            else:
                character.respawn()
            enemys.clear()
            badguys.clear()
            walls.clear()
            missiles.clear()

        #보물상자 관련: 적들이 다 죽고 보물상자 조건(3배수 스테이지)어야 생성
        if ((len(enemys) == 0) and (treasure.act == True)):
            treasure.draw()

            if treasure.touch():
                pygame.mixer.Sound.play(treasure_sound)
                rewards = (random.randint(1,4)) #보상 랜덤 뽑기
                treasure.reward(rewards)
                treasure.act = False
                treasure_txt = True

        tt = 0
        if theif.hp != 0 and stage >= 3:
            while tt < len(missiles): #미사일과 도둑이 닿으면 hp 1 감소
                if theif.hit(missiles[tt]):
                    del missiles[tt]
                    theif.hp -= 1
                    print(theif.hp)
                    theif.x = random.randint(100,1800)
                    if stage == 6:
                        theif.y = random.randint(100, 800)
                    tt -= 1
                tt+=1
        
        if theif.hp == 0: # hp0돼면 ㅌㅌ
            theif.stage3_move(theif.x)
            if stage == 7:
                enemys.clear()
                badguys.clear()
                walls.clear()
                missiles.clear()
                screen.blit(clear_News, (0, 0))

        e = 0 # 포탑 판단
        while e < len(enemys):
            m_ = 0
            enemys[e].draw()

            while m_ < len(missiles): #캐릭터의 미사일과 충돌하면 체력 1 감소
                if enemys[e].hit(missiles[m_]):
                    enemys[e].hp -= (1 + character.damage)
                    del missiles[m_]
                    j -= 1
                m_ += 1
            
            if time.time() - enemys[e].last_badguy_spawn_time > 1.5: #만약 포탑 사정거리 범위 내에 캐릭터가 있다면
                if (character.x - fire_range < enemys[e].x and character.x + fire_range + 40 > enemys[e].x + 40) or (character.y - fire_range < enemys[e].y and character.y + fire_range + 40 > enemys[e].y + 40):
                    enemys[e].fire()
                    enemys[e].last_badguy_spawn_time = time.time()

            if enemys[e].hp <= 0: #체력이 0이하가 되면 삭제
                    del enemys[e]
            e += 1
        
        ra = random.random()
        if time.time() - last_trash_spawn_time > ra + ddd and stage == 7: #만약 포탑 사정거리 범위 내에 캐릭터가 있다면
                    if spawn == True:
                        if theif.x > character.x: #오른쪽 방향을 보게 해야함
                            theif.t = "attack"   
                            theif.draw2()

                        if theif.x < character.x: #왼쪽 방향을 보게 해야함
                            theif.t = "attack" 
                            theif.draw()
                        theif.fire()
                        ddd -= 0.002
                        last_trash_spawn_time = time.time()

        i = 0 #포탑 총알 판단: 그리기, 화면 넘어가면 삭제
        while i < len(badguys):
            badguys[i].move()
            badguys[i].draw()

            if badguys[i].off_screen():
                del badguys[i]
                i -= 1
            i += 1

        i = 0 #포탑 총알 판단: 캐릭터와 충돌 했을 때 hp감소, 삭제
        while i < len(badguys):
            if badguys[i].touching_c(character): #만약 포탑 총알과 캐릭터가 닿았다면
                del badguys[i]
                character.hp -= 1
                i -= 1
            i += 1

        b = 0 #보스 판단
        while b < len(boss):
            m_ = 0
            boss[b].draw()

            while m_ < len(missiles): #미사일과 보스가 닿으면 hp 1 감소
                if boss[b].hit(missiles[m_]):
                    boss[b].hp -= (1 + character.damage)
                    del missiles[m_]
                    j -= 1
                m_ += 1

            if time.time() - boss[b].last_badguy_spawn_time > 1:
                boss[b].fire_big()
                boss[b].fire_small()
                boss[b].last_badguy_spawn_time = time.time()

            if boss[b].hp <= 0: #보스 체력이 0 이하가 되면 삭제
                    del boss[b]
            b += 1

        ib = 0 #보스 총알 판단: 그리기, 화면 넘어가면 삭제
        while ib < len(boss_missiles):
            boss_missiles[ib].move()
            boss_missiles[ib].draw()
            if boss_missiles[ib].off_screen():
                del boss_missiles[ib]
                ib -= 1
            ib += 1
        
        ib = 0 #보스 총알 판단: 캐릭터와 충돌 했을 때 hp감소, 삭제
        while ib < len(boss_missiles):
            if boss_missiles[ib].touching_c(character):
                del boss_missiles[ib]
                character.hp -= 1
                ib -= 1
            ib += 1

        w = 0 # 벽 판단: 그리기, 캐릭터 미사일과 충돌 했을 대 hp 감소, 삭제
        while w < len(walls):
            m = 0
            index = 0
            walls[w].draw()
            
            while m < len(missiles): #미사일과 충돌했을 때 hp 감소
                if walls[w].hit(missiles[m]):
                    walls[w].hp -= (1 + character.damage)
                    del missiles[m]
                    j -= 1
                
                if walls[w].hp <= stage * 6 / 2: #벽의 체력(stage * 6)이 절반이 되면 금간 이미지로 변경
                    walls[w].wall_state=wall_broken
                m += 1

            if walls[w].hp <= 0: #벽 체력이 0 이하가 되면 삭제(밑에도 추가하면 리스트 오류남)
                del walls[w]
            w += 1

        w = 0 # 벽 판단: 그리기, 포탑 미사일과 충돌 했을 대 hp 감소, 삭제
        while w < len(walls):
            index = 0
            walls[w].draw()
            
            while index < len(badguys):
                if walls[w].hit(badguys[index]):
                    walls[w].hp -= 1
                    del badguys[index]
                    j -= 1
                
                if walls[w].hp <= stage * 6 / 2:
                    walls[w].wall_state=wall_broken
                index += 1
            w += 1

        j = 0 #캐릭터 미사일 판단: 그리기, 화면 밖으로 나가면 삭제하기
        while j < len(missiles):
            missiles[j].move()
            if missiles[j].off_screen():
                del missiles[j]
                j -= 1
            j += 1

        #기본 인터페이스 정보
        if stage >= 1 and stage <= 10:

            hp_str_text = font3.render('HP', True, (255,128,128))
            screen.blit(hp_str_text, (10,10))
            hp_text = font3.render(str(int(character.hp)), True, (255,128,128))
            screen.blit(hp_text, (70,10))

        #캐릭터의 체력이 0이되어 게임 오버되었을 때 각종 게임 정보들 화면에 띄우기
        if character.hp <= 0:
                enemys.clear()
                badguys.clear()
                walls.clear()
                stage_music_loop.stop()
                screen.blit(bad_News,(0,0))
                Button(Main_Buttun,210,620,313,97,Main_Buttun,210,620,'replay')

                score = (character.hp * 100) - (int(start_time - time.time())) #점수 계산
                if high_score < score:
                        high_score = score

                #점수 화면에 띄우기

                mapcounter += 1
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit() # X누르면 나가기

                    if pygame.mouse.get_pressed()[0] and Main_Buttun_rect.collidepoint(pygame.mouse.get_pos()):
                        last_fire = 0
                        stage = 0
                        score = 0
                        fff
                        ggg

                        mapcounter = 1
                        missile_speed = 10
                        character = Character()
                        Map = Stage()
                        theif = Theif("")
                        treasure = Treasure()
                        badguys = []
                        enemys = []
                        walls = []
                        boss = []
                        cave_trashs = []
                        space_trashs = []
                        missiles = []
                        boss_missiles = []
                        last_trash_spawn_time = 0
                        ggg = 0
                        fff = 0
                        ddd = 0.9
                        Map.homescreen()
                        time.sleep(0.5)
                        break

                    elif pygame.mouse.get_pressed()[0] and end_rect.collidepoint(pygame.mouse.get_pos()):
                        sys.exit()
                        
                    pygame.display.update() #화면에 나타내기

    pygame.display.update() #화면 업데이트