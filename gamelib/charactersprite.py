import pygame
import action
import sceneobject

class CharacterSprite(sceneobject.SceneObject):
    """
        This class represents any sprite directly controlled by user keyboard or mouse input.
        Currently, it contains the following simple actions:
            Key:            Action:
            Left            Walk left
            Shift+Left      Run left
            Right           Walk right
            Shift+Right     Run right
            Up              Jump up
    """
    def __init__(self, args):
        so_args = {'pos':args['STARTPOS'], 'filename':args['FILENAME']}
        sceneobject.SceneObject.__init__(self,so_args)
        self.spritesheet = self.image
        #self.spritesheet_ids = spritesheet_ids
        self.jump_height = args['JUMPHEIGHT']
        self.sprite_width = args['WIDTH']
        self.sprite_height = args['HEIGHT']
        self.rect = self.image.get_rect()
        self.sprite_rect = pygame.rect.Rect(self.x, self.y, self.sprite_width, self.sprite_height)
        self.actions = args['ACTIONS']
        self.walk_step = self.sprite_width*0.0125
        self.fast_factor = 3
        self.fall_step = self.sprite_height*0.0125
        self.state = {
                        'steps'         : 0,
                        'fallcount'     : 0,
                        'action'        : 'STAND',
                        'last'          : 'STAND',
                        'lastisdone'    : False,
                        'left'          : False,
                        'running'       : False,
                        'jumping'       : False,
                        'falling'       : False,
                        'fallingfast'   : False,
                        'landing'       : False,
                        'walking'       : False,
                        'rdown'         : False,
                        'ldown'         : False,
                     }
    
    def left(self):
        self.state['left'] = True
    
    def right(self):
        self.state['left'] = False
    
    def stand(self):
        self.state['jumping'] = self.state['running'] = self.state['falling'] = self.state['fallingfast'] = self.state['landing'] = self.state['walking'] = False
    
    def jump(self):
        self.state['jumping'] = True
    
    def fall(self):
        self.nojump()
        self.state['falling'] = True
    
    def fallfast(self):
        self.nojump()
        self.state['fallingfast'] = True
    
    def run (self):
        self.state['running'] = True
    
    def land(self):
        self.nofall()
        self.state['fallcount'] = 1
        self.state['landing'] = True
    
    def walk(self):
        self.state['walking'] = True
    
    def nojump(self):
        self.state['jumping'] = False
    
    def nofall(self):
        self.state['falling'] = False
    
    def nofallfast(self):
        self.state['fallingfast'] = False
    
    def norun (self):
        self.state['running'] = False
    
    def noland(self):
        self.state['landing'] = False
    
    def nowalk(self):
        self.state['walking'] = False
    
    
    def handle(self, event):
        """
            Handle user input events
        """
        if   event.type == pygame.KEYDOWN:
            if   event.key == pygame.K_LEFT:
                self.left()
                self.state['ldown'] = True
                ''' Previous functionality if desired, but this has been deprecated and moved to the update() function.
                if not self.state['falling']:
                    mods = pygame.key.get_mods()
                    # Hold shift (left or right) to run
                    if  mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_RSHIFT:
                        self.run()
                        self.nowalk()
                    else:
                        self.walk()
                        self.norun()
                '''
                
            elif event.key == pygame.K_RIGHT:
                self.right()
                self.state['rdown'] = True
                if not (self.state['jumping'] or self.state['falling'] or self.state['fallingfast'] or self.state['landing']):
                    '''  Previous functionality if desired, but this has been deprecated and moved to the update() function.
                    
                    mods = pygame.key.get_mods()
                    # Hold shift (left or right) to run
                    if  mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_RSHIFT:
                        self.run()
                    else:
                        self.walk()
                    '''
                
            elif event.key == pygame.K_UP:
                self.jump()
            
            # TODO: Consider adding in Smash Bros. style falling through the floor.
            # elif event.key == pygame.K_DOWN:
            #     self.fall()
            
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if event.key == pygame.K_LEFT :
                    self.state['ldown'] = False
                    if self.state['rdown']:
                        self.right()
                elif event.key == pygame.K_RIGHT:
                    self.state['rdown'] = False
                    if self.state['ldown']:
                        self.left()
                if not (self.state['jumping'] or self.state['falling'] or self.state['fallingfast'] or self.state['landing']) and not self.state['ldown'] and not self.state['rdown']:
                    self.stand()
                if not self.state['running']:
                    self.state['steps'] = 0
        
        if self.state['ldown'] or self.state['rdown']: self.walk()
    
    
    def update(self):
        """
            Determine the action to draw and how to change the character based on it.
        """
        
        # Some state information for debugging purposes; generally not necessary to print.
        #print "Walking:", self.state['walking'], " Running:", self.state['running'], " Jumping:", self.state['jumping']
        
        # The action currently in process has reached its last sprite image and is about to loop.
        # Certain actions require an interruption. Those interruptions are placed here.
        if self.state['lastisdone']:
            # Landing
            if   self.state['last'] == 'LAND':
                # Landing should only loop once, then transition to standing
                self.stand()
                # Make sure to check whether the character should be walking
                if self.state['ldown'] or self.state['rdown']: self.walk()
            
            # Jumping
            elif self.state['last'] == 'JUMP':
                # Jumping should loop on the final frame until a predetermined height is reached
                if self.y > self.jump_height+self.init_pos[1]:
                    self.actions['JUMP'].curr_step = self.actions['JUMP'].step_duration * (self.actions['JUMP'].num_steps - 2)
                # Once the height is reached, transition to falling
                else:
                    self.nojump()
                    self.fall()
            
            # Falling
            elif self.state['last'] == 'FALL':
                # Falling should loop until one of two things happens:
                # If the floor has not yet been reached,
                if self.y < self.init_pos[1]:
                    # Increase the fall counter
                    self.state['fallcount'] += 1
                    # Check to see whether a predetermined number of loops has been reached
                    # If it has, transition to falling fast
                    if self.state['fallcount'] > 100:
                        self.state['fallcount'] = 0
                        self.nofall()
                        self.fallfast()
                # If the floor has been reached or surpassed, move to floor height and transition to landing
                else:
                    self.y = self.init_pos[1]
                    self.nofall()
                    self.land()
            
            # Falling Fast
            elif self.state['last'] == 'FALL_FAST':
                # If the floor has been reached or surpassed, move to floor height and transition to landing
                if self.y >= self.init_pos[1]:
                    self.y = self.init_pos[1]-self.sprite_height
                    self.nofallfast()
                    self.land()

            # Always reset the 'lastisdone' flag
            self.state['lastisdone'] = False
        
        
        
        
        
        
        # Default to standing, unless something below changes the state
        self.state['action'] = 'STAND'
        
        # Walking
        if self.state['walking']:
            # If either shift key is held, set to running
            mods = pygame.key.get_mods()
            if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_RSHIFT:
                self.nowalk()
                self.run()
            # Otherwise, move forward a preset distance and render the WALK action sprite
            else:
                self.state['action'] = 'WALK'
                self.move((self.walk_step if not self.state['left'] else -self.walk_step, 0))
        
        # Running
        if self.state['running']:
            # Move forward a preset distance and render the RUN action sprite
            self.state['action'] = 'RUN'
            self.move(((self.walk_step if not self.state['left'] else -self.walk_step)*self.fast_factor, 0))
            mods = pygame.key.get_mods()
            # If shift is no longer being held, make sure the next frame walking happens
            if not (mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_RSHIFT):
                self.norun()
                self.walk()
        
        # Jumping
        if self.state['jumping']: 
            # Move up a preset distance and render the JUMP action sprite
            self.state['action'] = 'JUMP'
            self.move((0,-self.fall_step))
        
        # Falling
        # This action currently happens only as the result of a jump action
        if self.state['falling']:
            # Move down a preset distance and render the FALL action sprite
            self.state['action'] = 'FALL'
            self.move((0,self.fall_step))
        
        # Falling Fast
        # This action is intended to happen only when the character has been falling for a while
        if self.state['fallingfast']:
            # Move down a little farther than in a standard falling action and render the FALL_FAST action sprite
            self.state['action'] = 'FALL_FAST'
            self.move((0,self.fall_step*fast_factor))
        
        # Landing
        # This action should only happen after falling
        if self.state['landing']:
            self.state['action'] = 'LAND'
        
        if self.actions[self.state['action']].curr_step/self.actions[self.state['action']].step_duration == self.actions[self.state['action']].num_steps - 1:
            self.state['lastisdone'] = True
        
        if self.state['action'] != self.state['last']:
            self.actions[self.state['last']].reset()
        
        self.state['last'] = self.state['action']
        

    
    def drawable(self):
        currscene = pygame.Surface((self.sprite_width,self.sprite_height), flags=pygame.surface.SRCALPHA)
        currscene.fill((0,0,0,0))
        self.draw(currscene)
        return currscene
    
    
    def draw(self, surface):
        if self.spritesheet == None: return
        flip = self.state['left']
        tmpsprite = self.image if not flip else pygame.transform.flip(self.image, True, False)
        tmprect = pygame.Rect(
                    # If facing left, sprite's left position becomes img.width-spriteid*spritewidth ; else, it's just spriteid*spritewidth
                    self.sprite_width*self.actions[self.state['action']].id if not flip else self.rect.width-self.sprite_width-self.sprite_width*self.actions[self.state['action']].id,
                    self.sprite_height*self.actions[self.state['action']].next(),
                    self.sprite_width,
                    self.sprite_height
                  )
        #print flip, tmprect
        surface.blit(tmpsprite, self.pos(), tmprect)
    
    
    def reset(self):
        sceneobject.SceneObject.reset(self)
        self.state['last'] = 'STAND'
        self.state['action'] = 'STAND'
