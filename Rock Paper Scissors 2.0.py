import random, time, os

rock_rock = [
'''  


                     ..=8MMMMMMMM..                         
                    .MNMM  ..,.INMM.                        
                .. MMM=..........,MMMMMMM7 ..               
     .......... .MMM....  MM.   . MMMMMMMMMM...             
...............MMN. . ..,,MM..   .MM.  . ,.MM..             
.IMMMMMMMMMMMMNN8,.   .  .MM .    MM. .  .=MM .             
.IM7...        .      ...,MM.     MMMMMMMMMM.               
.IM7 .                  .DMM..    MNMMMMMMMMM..             
.IM7 .         ...    . 7DDN..    MM     ..NM:.             
.IM7 .        .MM7. ..IMMNMM..   .MM.......8M=              
.IM7 .        .,NMMMMMM8...8MI  .,MM......MMM .             
.IM7 .         ........:,,,,MMMMMMMMMMMMMMMZ...             
.IM7 .                .........MM=...  . ,MM.               
.IM7 .                 .    ,. MM.    .. .MM,               
.IM7.  ..     ...     .. ,.,. .OMM.......NMM .              
 INMMMMMMMMMMMMN .       .......MNMMMMMMMNN..               
 ,$O8DNNMMMMMMMMN,.   . .......MM:...  ..MM.                
     .    .   ..NMM?, ..,.. ...MM~.... ..MM..               
                  MMMMM8MDMMM8MMMMMMMMMMMMZ..  
                          
                           
                            
                                     ''',
    '''                      
                            
                           
                    . ..MMMMMMMM8=..                      
                        MMNI.,....MMNM.                     
              ...7MMMMMMM...... ....=MMM..                  
             ..MMNMMMMMMM .   .MM...  .MMM. ...........     
            . MM., .  .MM    . MM,,.. . .MNM..............  
              MM=.    .MM     .MM ...   .,OMNMMMMMMMMMMMM7. 
            . .MMMMMMMMMM    ..MM,...      .          .7MI. 
            ..MMMMMMMMMNM  .  .MMD.       .          . 7MI. 
            .:MD.     .MM    ..NDD7 .                . 7MI. 
             =MO.......MM. .   MMNMM7. .,7MM         . 7MI. 
            ..MMM.  . .MM,...IM8. .8MMMMMMN.         . 7MI. 
            . .ZMMMMMMMMMMMMMMM,,,,:.....  .         . 7MI. 
              .MM, ..... =MM.. .. ..                 . 7MI. 
              ,MN. .     .MM  , .  .                 . 7MI. 
              .MMN ......MMO...,.,  .         .      . 7MI. 
              ..NNMMMMMMMMM..... .        .NMMMMMMMMMMMMMI. 
              ..MN..     :MM,......   . ,,NMMMMMMMMNND88$,. 
              ..MM. .....~MM. ....,.. .?MMM.. .. .   ..   . 
               .ZMMMMMMMMMMMM8MMMDM8MMMMM ..  
                           
                           
                             
                           '''
]
paper_rock = ['''                                           
                          .MMMM$. .                         
                        .MMM..DNN.                          
                      ..MMM   .MMM..                        
                    . MMM. .  ..MM .                        
                  ..:MMZ.      MMD..                        
                ...MMM..     .MMMMMMMMMMMMMMMMMMMMM$.....   
  .            . DMMO .    .MMMMMMMMMMMMMMMMMMMMMMMMMMO .   
               ,MMM.      .MNN. .....................MMO    
..MMMMMMMMMMMMMMM ..    .MMM,                       .OMM.   
 .MMMMMMMMMMMMMO.        MM?..    .. ............. .,MM,    
  MM       ...         . 8MM     ..MMMMMMMMMMMMMMMMMMMM~.   
  MM.                 ...NM=                     . ...MMM.  
  MM.          ...  . ..MMM.       ..                ..ZMI. 
  MM.         ..MMM ..MMMM,.                          .MM   
  MM.          . MMMMMMN,...     . MMMMMMMMMMMMMMMMMMMMM:.. 
  MM.            ...              ,.~~~~~~~~~~~~~~IMMM.     
  MM.                                            .. MMN     
  MM.                              .               .MMN.    
 .MM...... .  ....                .MMMMMMMMMMMMMMMMMMM .    
 .MMMMMMMMMMMMMNN ..               MMMMMMMMMMMMMMMMN....    
.. .......,,,,,MMN .             .  ..   ... ..MM... ...    
    .......     .MMMM........................,OMN..         
               . ..ONMMMMMMMMMMMMMMMMMMMMMMMMMMM.  .        
                                                     
                                                      ''',
           '''        
           
           
        
                           
                    . ..MMMMMMMM8=..                      
                        MMNI.,....MMNM.                     
              ...7MMMMMMM...... ....=MMM..                  
             ..MMNMMMMMMM .   .MM...  .MMM. ...........     
            . MM., .  .MM    . MM,,.. . .MNM..............  
              MM=.    .MM     .MM ...   .,OMNMMMMMMMMMMMM7. 
            . .MMMMMMMMMM    ..MM,...      .          .7MI. 
            ..MMMMMMMMMNM  .  .MMD.       .          . 7MI. 
            .:MD.     .MM    ..NDD7 .                . 7MI. 
             =MO.......MM. .   MMNMM7. .,7MM         . 7MI. 
            ..MMM.  . .MM,...IM8. .8MMMMMMN.         . 7MI. 
            . .ZMMMMMMMMMMMMMMM,,,,:.....  .         . 7MI. 
              .MM, ..... =MM.. .. ..                 . 7MI. 
              ,MN. .     .MM  , .  .                 . 7MI. 
              .MMN ......MMO...,.,  .         .      . 7MI. 
              ..NNMMMMMMMMM..... .        .NMMMMMMMMMMMMMI. 
              ..MN..     :MM,......   . ,,NMMMMMMMMNND88$,. 
              ..MM. .....~MM. ....,.. .?MMM.. .. .   ..   . 
               .ZMMMMMMMMMMMM8MMMDM8MMMMM ..  
                           
                           
                             
                           ''']
scissors_rock = ['''                        .  .     .                 .         
                     . .,MMMMMM,  .                         
                  . ,.MMNMD::OMMMMZ  . .. .....~DMMM$.      
                 . .MMMD .      .NN=...7MMMMMMMMMMMMMN..    
               ...MMM  ...MN     .MMMMMMMM=....     .MM,    
  .             MMM+.    .MM.  ...MM.....       .   .MM.    
..MMMMMMMMMMMMMMM+.     . MM.    .MM. . .. ... .$MMMMN..    
.MMMMMMMMMMMMMM$.       ..MM.  ...MM. IMMMMMMMMMMMM~.   .   
.MM..            .      ..MM   ...MMMMMMMMMMMMMMMMMMMMD..   
.MM.                  .. MMM.  .. MM.........,:~+IZ8NMMMD.  
.MM.          . . ..  ..MMMM,   ..MM.    . .. .. .  ...MM   
.MM.          .7MMM,..DMMM.MN.    MM ..       .       .MM   
.MM.          ...MMMMMMM...~DMN.~NMMMMMMMMMMNND88OOZOOMMM   
.MM.                ..      .NNMMMMMMMMMMNMMMMMMMMMMMMM~ .  
.MM.                          .MM,. ... . MM+.... ..   .    
.MM,        ...                MMO........MM..              
.MM. ..       ..              ..MMMMMMMMMMMM,.              
.NMMMMMMMMMMMMMN,.             .MMD?++++MND...              
..??++=:,,...,,NM+ ...  . .  . MMD.  .. .MM                 
    ............MMMMI. ........+MM.... .?MM.                
                 .=MMMMMMMMMMMMMMMMMMMMMMM.                 
                   
                                                            
                                              ''',
           '''        
                           
                    . ..MMMMMMMM8=..                      
                        MMNI.,....MMNM.                     
              ...7MMMMMMM...... ....=MMM..                  
             ..MMNMMMMMMM .   .MM...  .MMM. ...........     
            . MM., .  .MM    . MM,,.. . .MNM..............  
              MM=.    .MM     .MM ...   .,OMNMMMMMMMMMMMM7. 
            . .MMMMMMMMMM    ..MM,...      .          .7MI. 
            ..MMMMMMMMMNM  .  .MMD.       .          . 7MI. 
            .:MD.     .MM    ..NDD7 .                . 7MI. 
             =MO.......MM. .   MMNMM7. .,7MM         . 7MI. 
            ..MMM.  . .MM,...IM8. .8MMMMMMN.         . 7MI. 
            . .ZMMMMMMMMMMMMMMM,,,,:.....  .         . 7MI. 
              .MM, ..... =MM.. .. ..                 . 7MI. 
              ,MN. .     .MM  , .  .                 . 7MI. 
              .MMN ......MMO...,.,  .         .      . 7MI. 
              ..NNMMMMMMMMM..... .        .NMMMMMMMMMMMMMI. 
              ..MN..     :MM,......   . ,,NMMMMMMMMNND88$,. 
              ..MM. .....~MM. ....,.. .?MMM.. .. .   ..   . 
               .ZMMMMMMMMMMMM8MMMDM8MMMMM ..  
                           
                           
                             
                           ''']

paper_paper = ['''                                           
                          .MMMM$. .                         
                        .MMM..DNN.                          
                      ..MMM   .MMM..                        
                    . MMM. .  ..MM .                        
                  ..:MMZ.      MMD..                        
                ...MMM..     .MMMMMMMMMMMMMMMMMMMMM$.....   
  .            . DMMO .    .MMMMMMMMMMMMMMMMMMMMMMMMMMO .   
               ,MMM.      .MNN. .....................MMO    
..MMMMMMMMMMMMMMM ..    .MMM,                       .OMM.   
 .MMMMMMMMMMMMMO.        MM?..    .. ............. .,MM,    
  MM       ...         . 8MM     ..MMMMMMMMMMMMMMMMMMMM~.   
  MM.                 ...NM=                     . ...MMM.  
  MM.          ...  . ..MMM.       ..                ..ZMI. 
  MM.         ..MMM ..MMMM,.                          .MM   
  MM.          . MMMMMMN,...     . MMMMMMMMMMMMMMMMMMMMM:.. 
  MM.            ...              ,.~~~~~~~~~~~~~~IMMM.     
  MM.                                            .. MMN     
  MM.                              .               .MMN.    
 .MM...... .  ....                .MMMMMMMMMMMMMMMMMMM .    
 .MMMMMMMMMMMMMNN ..               MMMMMMMMMMMMMMMMN....    
.. .......,,,,,MMN .             .  ..   ... ..MM... ...    
    .......     .MMMM........................,OMN..         
               . ..ONMMMMMMMMMMMMMMMMMMMMMMMMMMM.  .        
                                                     
                                                      ''',
           '''     
                          .$MMMM...                         
                        ..NND..MMM.                         
                        .MMM. ..MMM..                       
                       ..MM..  . .MMM                       
                       . DMM      .ZMM:..                   
  .  ..ZMMMMMMMMMMMMMMMMMMMMM      ..MMM.                   
   .ZMMMMMMMMMMMMMMMMMMMMMMMMMM..   . ONMD..                
 . OMM....................  .NNM.      .MMM,                
   MMO.                      .,MMM.    ...MMMMMMMMMMMMMMM.. 
   ,MM,.. ...............      ?MM       ..OMMMMMMMMMMMMM . 
 ..~MMMMMMMMMMMMMMMMMMMM..     MM8 .        ....       MM   
 .MMM.....                    .=MM.                    MM   
 IMZ.                 ..       .MMM . .  ..            MM   
  MM.                           .MMNM ..NMM.           MM   
 .,MMMMMMMMMMMMMMMMMMMMN.       ..,NMMMMMM..           MM   
   ..MMMI~:~~~~~~~~~~~:.,          .. ....             MM   
   .NMM...                                             MM   
  ..NMM.               .                               MM   
     MMMMMMMMMMMMMMMMMMM.                  ..    ... ..MM.  
      .NMMMMMMMMMMMMMMMM .             .  NNMMMMMMMMMMMMM   
   .  ... MM . .....  . .               .NMM.,,,,....... .. 
         .NMO.........................MMMM .    .......     
           MMMMMMMMMMMMMMMMMMMMMMMMMMMNZ.. . 
           ''']

scissors_scissors = ['''                        .  .     .                         
                     . .,MMMMMM,  .                         
                  . ,.MMNMD::OMMMMZ  . .. .....~DMMM$.      
                 . .MMMD .      .NN=...7MMMMMMMMMMMMMN..    
               ...MMM  ...MN     .MMMMMMMM=....     .MM,    
  .             MMM+.    .MM.  ...MM.....       .   .MM.    
..MMMMMMMMMMMMMMM+.     . MM.    .MM. . .. ... .$MMMMN..    
.MMMMMMMMMMMMMM$.       ..MM.  ...MM. IMMMMMMMMMMMM~.   .   
.MM..            .      ..MM   ...MMMMMMMMMMMMMMMMMMMMD..   
.MM.                  .. MMM.  .. MM.........,:~+IZ8NMMMD.  
.MM.          . . ..  ..MMMM,   ..MM.    . .. .. .  ...MM   
.MM.          .7MMM,..DMMM.MN.    MM ..       .       .MM   
.MM.          ...MMMMMMM...~DMN.~NMMMMMMMMMMNND88OOZOOMMM   
.MM.                ..      .NNMMMMMMMMMMNMMMMMMMMMMMMM~ .  
.MM.                          .MM,. ... . MM+.... ..   .    
.MM,        ...                MMO........MM..              
.MM. ..       ..              ..MMMMMMMMMMMM,.              
.NMMMMMMMMMMMMMN,.             .MMD?++++MND...              
..??++=:,,...,,NM+ ...  . .  . MMD.  .. .MM                 
    ............MMMMI. ........+MM.... .?MM.                
                 .=MMMMMMMMMMMMMMMMMMMMMMM.                 
                   
                                                            
                                              ''',
           '''                               .                           
                        .. .MMMMMM,...                      
      $MMMD~....  .... .ZMMMMO::DMNMM ,.                    
   ..NMMMMMMMMMMMMM$...=NN  .  .  .8MMM. .                  
   ,MM,.   .....=MMMMMMMM..   .NM. ...MMM  .                
   .MM .  .       .....MM..  ..MM..   .+MMM .           ..  
    .NMMMM$..... .... .MM.    .MM .     .+MMMMMMMMMMMMMMM.. 
 .     ~MMMMMMMMMMMMI .MM..   .MM.         $MMMMMMMMMMMMMM. 
  ..DMMMMMMMMMMMMMMMMMMMM..   .MM.        ..           .MM. 
 .NMMMN8ZI+~:,.........MM..  ..MMM .                   .MM. 
..MM ..  . .. ....   ..MM...  ,MMMM    . ..            .MM. 
  MM. ...           .. MM... .MM.MMMD .:MMMI           .MM. 
 .MMMOOOOO88DNNMMMMMMMMMMN~ DMD~ ,.MMMMMMM..           .MM. 
   ~MMMMMMMMMMMMMNMMMMMMMMMMNM.      ..                .MM. 
   . . .  ... +MM.. ...  ,MM.                          .MM. 
              .MM. ......OMM                ....      ..MM. 
             .,MMMMMMMMMMNM.             . .        ....MM. 
              ..DNM=+++?DNM..             ,NMMMMMMMMMMMMMM  
               .MM. .... DMM.. .      .  +MN,,..,,,~=++?? . 
               .MM?. ....MM=. . ..... IMMMM............     
              . .MMMMMMMMMMMMMMMMMMMMMMM~.                  
                        ''']

rock_paper = [''' 


                     ..=8MMMMMMMM..                         
                    .MNMM  ..,.INMM.                        
                .. MMM=..........,MMMMMMM7 ..               
     .......... .MMM....  MM.   . MMMMMMMMMM...             
...............MMN. . ..,,MM..   .MM.  . ,.MM..             
.IMMMMMMMMMMMMNN8,.   .  .MM .    MM. .  .=MM .             
.IM7...        .      ...,MM.     MMMMMMMMMM.               
.IM7 .                  .DMM..    MNMMMMMMMMM..             
.IM7 .         ...    . 7DDN..    MM     ..NM:.             
.IM7 .        .MM7. ..IMMNMM..   .MM.......8M=              
.IM7 .        .,NMMMMMM8...8MI  .,MM......MMM .             
.IM7 .         ........:,,,,MMMMMMMMMMMMMMMZ...             
.IM7 .                .........MM=...  . ,MM.               
.IM7 .                 .    ,. MM.    .. .MM,               
.IM7.  ..     ...     .. ,.,. .OMM.......NMM .              
 INMMMMMMMMMMMMN .       .......MNMMMMMMMNN..               
 ,$O8DNNMMMMMMMMN,.   . .......MM:...  ..MM.                
     .    .   ..NMM?, ..,.. ...MM~.... ..MM..               
                  MMMMM8MDMMM8MMMMMMMMMMMMZ..  
                          
                           
                            
                                      ''',
           '''     
                          .$MMMM...                         
                        ..NND..MMM.                         
                        .MMM. ..MMM..                       
                       ..MM..  . .MMM                       
                       . DMM      .ZMM:..                   
  .  ..ZMMMMMMMMMMMMMMMMMMMMM      ..MMM.                   
   .ZMMMMMMMMMMMMMMMMMMMMMMMMMM..   . ONMD..                
 . OMM....................  .NNM.      .MMM,                
   MMO.                      .,MMM.    ...MMMMMMMMMMMMMMM.. 
   ,MM,.. ...............      ?MM       ..OMMMMMMMMMMMMM . 
 ..~MMMMMMMMMMMMMMMMMMMM..     MM8 .        ....       MM   
 .MMM.....                    .=MM.                    MM   
 IMZ.                 ..       .MMM . .  ..            MM   
  MM.                           .MMNM ..NMM.           MM   
 .,MMMMMMMMMMMMMMMMMMMMN.       ..,NMMMMMM..           MM   
   ..MMMI~:~~~~~~~~~~~:.,          .. ....             MM   
   .NMM...                                             MM   
  ..NMM.               .                               MM   
     MMMMMMMMMMMMMMMMMMM.                  ..    ... ..MM.  
      .NMMMMMMMMMMMMMMMM .             .  NNMMMMMMMMMMMMM   
   .  ... MM . .....  . .               .NMM.,,,,....... .. 
         .NMO.........................MMMM .    .......     
           MMMMMMMMMMMMMMMMMMMMMMMMMMMNZ.. . 
           ''']

rock_scissors = [''' 


                     ..=8MMMMMMMM..                         
                    .MNMM  ..,.INMM.                        
                .. MMM=..........,MMMMMMM7 ..               
     .......... .MMM....  MM.   . MMMMMMMMMM...             
...............MMN. . ..,,MM..   .MM.  . ,.MM..             
.IMMMMMMMMMMMMNN8,.   .  .MM .    MM. .  .=MM .             
.IM7...        .      ...,MM.     MMMMMMMMMM.               
.IM7 .                  .DMM..    MNMMMMMMMMM..             
.IM7 .         ...    . 7DDN..    MM     ..NM:.             
.IM7 .        .MM7. ..IMMNMM..   .MM.......8M=              
.IM7 .        .,NMMMMMM8...8MI  .,MM......MMM .             
.IM7 .         ........:,,,,MMMMMMMMMMMMMMMZ...             
.IM7 .                .........MM=...  . ,MM.               
.IM7 .                 .    ,. MM.    .. .MM,               
.IM7.  ..     ...     .. ,.,. .OMM.......NMM .              
 INMMMMMMMMMMMMN .       .......MNMMMMMMMNN..               
 ,$O8DNNMMMMMMMMN,.   . .......MM:...  ..MM.                
     .    .   ..NMM?, ..,.. ...MM~.... ..MM..               
                  MMMMM8MDMMM8MMMMMMMMMMMMZ..  
                          
                           
                            
                                      ''',
           '''                               
           
                        .. .MMMMMM,...                      
      $MMMD~....  .... .ZMMMMO::DMNMM ,.                    
   ..NMMMMMMMMMMMMM$...=NN  .  .  .8MMM. .                  
   ,MM,.   .....=MMMMMMMM..   .NM. ...MMM  .                
   .MM .  .       .....MM..  ..MM..   .+MMM .           ..  
    .NMMMM$..... .... .MM.    .MM .     .+MMMMMMMMMMMMMMM.. 
 .     ~MMMMMMMMMMMMI .MM..   .MM.         $MMMMMMMMMMMMMM. 
  ..DMMMMMMMMMMMMMMMMMMMM..   .MM.        ..           .MM. 
 .NMMMN8ZI+~:,.........MM..  ..MMM .                   .MM. 
..MM ..  . .. ....   ..MM...  ,MMMM    . ..            .MM. 
  MM. ...           .. MM... .MM.MMMD .:MMMI           .MM. 
 .MMMOOOOO88DNNMMMMMMMMMMN~ DMD~ ,.MMMMMMM..           .MM. 
   ~MMMMMMMMMMMMMNMMMMMMMMMMNM.      ..                .MM. 
   . . .  ... +MM.. ...  ,MM.                          .MM. 
              .MM. ......OMM                ....      ..MM. 
             .,MMMMMMMMMMNM.             . .        ....MM. 
              ..DNM=+++?DNM..             ,NMMMMMMMMMMMMMM  
               .MM. .... DMM.. .      .  +MN,,..,,,~=++?? . 
               .MM?. ....MM=. . ..... IMMMM............     
              . .MMMMMMMMMMMMMMMMMMMMMMM~.                  
                        
           ''']

paper_scissors = ['''
                         .MMMM$. .                         
                        .MMM..DNN.                          
                      ..MMM   .MMM..                        
                    . MMM. .  ..MM .                        
                  ..:MMZ.      MMD..                        
                ...MMM..     .MMMMMMMMMMMMMMMMMMMMM$.....   
  .            . DMMO .    .MMMMMMMMMMMMMMMMMMMMMMMMMMO .   
               ,MMM.      .MNN. .....................MMO    
..MMMMMMMMMMMMMMM ..    .MMM,                       .OMM.   
 .MMMMMMMMMMMMMO.        MM?..    .. ............. .,MM,    
  MM       ...         . 8MM     ..MMMMMMMMMMMMMMMMMMMM~.   
  MM.                 ...NM=                     . ...MMM.  
  MM.          ...  . ..MMM.       ..                ..ZMI. 
  MM.         ..MMM ..MMMM,.                          .MM   
  MM.          . MMMMMMN,...     . MMMMMMMMMMMMMMMMMMMMM:.. 
  MM.            ...              ,.~~~~~~~~~~~~~~IMMM.     
  MM.                                            .. MMN     
  MM.                              .               .MMN.    
 .MM...... .  ....                .MMMMMMMMMMMMMMMMMMM .    
 .MMMMMMMMMMMMMNN ..               MMMMMMMMMMMMMMMMN....    
.. .......,,,,,MMN .             .  ..   ... ..MM... ...    
    .......     .MMMM........................,OMN..         
               . ..ONMMMMMMMMMMMMMMMMMMMMMMMMMMM.  .   ''',
           '''      
           
           
           
                        .. .MMMMMM,...                      
      $MMMD~....  .... .ZMMMMO::DMNMM ,.                    
   ..NMMMMMMMMMMMMM$...=NN  .  .  .8MMM. .                  
   ,MM,.   .....=MMMMMMMM..   .NM. ...MMM  .                
   .MM .  .       .....MM..  ..MM..   .+MMM .           ..  
    .NMMMM$..... .... .MM.    .MM .     .+MMMMMMMMMMMMMMM.. 
 .     ~MMMMMMMMMMMMI .MM..   .MM.         $MMMMMMMMMMMMMM. 
  ..DMMMMMMMMMMMMMMMMMMMM..   .MM.        ..           .MM. 
 .NMMMN8ZI+~:,.........MM..  ..MMM .                   .MM. 
..MM ..  . .. ....   ..MM...  ,MMMM    . ..            .MM. 
  MM. ...           .. MM... .MM.MMMD .:MMMI           .MM. 
 .MMMOOOOO88DNNMMMMMMMMMMN~ DMD~ ,.MMMMMMM..           .MM. 
   ~MMMMMMMMMMMMMNMMMMMMMMMMNM.      ..                .MM. 
   . . .  ... +MM.. ...  ,MM.                          .MM. 
              .MM. ......OMM                ....      ..MM. 
             .,MMMMMMMMMMNM.             . .        ....MM. 
              ..DNM=+++?DNM..             ,NMMMMMMMMMMMMMM  
               .MM. .... DMM.. .      .  +MN,,..,,,~=++?? . 
               .MM?. ....MM=. . ..... IMMMM............     
              . .MMMMMMMMMMMMMMMMMMMMMMM~.                  
                        
           ''']

scissors_paper = ['''   



                     . .,MMMMMM,  .                         
                  . ,.MMNMD::OMMMMZ  . .. .....~DMMM$.      
                 . .MMMD .      .NN=...7MMMMMMMMMMMMMN..    
               ...MMM  ...MN     .MMMMMMMM=....     .MM,    
  .             MMM+.    .MM.  ...MM.....       .   .MM.    
..MMMMMMMMMMMMMMM+.     . MM.    .MM. . .. ... .$MMMMN..    
.MMMMMMMMMMMMMM$.       ..MM.  ...MM. IMMMMMMMMMMMM~.   .   
.MM..            .      ..MM   ...MMMMMMMMMMMMMMMMMMMMD..   
.MM.                  .. MMM.  .. MM.........,:~+IZ8NMMMD.  
.MM.          . . ..  ..MMMM,   ..MM.    . .. .. .  ...MM   
.MM.          .7MMM,..DMMM.MN.    MM ..       .       .MM   
.MM.          ...MMMMMMM...~DMN.~NMMMMMMMMMMNND88OOZOOMMM   
.MM.                ..      .NNMMMMMMMMMMNMMMMMMMMMMMMM~ .  
.MM.                          .MM,. ... . MM+.... ..   .    
.MM,        ...                MMO........MM..              
.MM. ..       ..              ..MMMMMMMMMMMM,.              
.NMMMMMMMMMMMMMN,.             .MMD?++++MND...              
..??++=:,,...,,NM+ ...  . .  . MMD.  .. .MM                 
    ............MMMMI. ........+MM.... .?MM.                
                 .=MMMMMMMMMMMMMMMMMMMMMMM.                 
                                    
                                                            
                                           ''',
           '''     
                          .$MMMM...                         
                        ..NND..MMM.                         
                        .MMM. ..MMM..                       
                       ..MM..  . .MMM                       
                       . DMM      .ZMM:..                   
  .  ..ZMMMMMMMMMMMMMMMMMMMMM      ..MMM.                   
   .ZMMMMMMMMMMMMMMMMMMMMMMMMMM..   . ONMD..                
 . OMM....................  .NNM.      .MMM,                
   MMO.                      .,MMM.    ...MMMMMMMMMMMMMMM.. 
   ,MM,.. ...............      ?MM       ..OMMMMMMMMMMMMM . 
 ..~MMMMMMMMMMMMMMMMMMMM..     MM8 .        ....       MM   
 .MMM.....                    .=MM.                    MM   
 IMZ.                 ..       .MMM . .  ..            MM   
  MM.                           .MMNM ..NMM.           MM   
 .,MMMMMMMMMMMMMMMMMMMMN.       ..,NMMMMMM..           MM   
   ..MMMI~:~~~~~~~~~~~:.,          .. ....             MM   
   .NMM...                                             MM   
  ..NMM.               .                               MM   
     MMMMMMMMMMMMMMMMMMM.                  ..    ... ..MM.  
      .NMMMMMMMMMMMMMMMM .             .  NNMMMMMMMMMMMMM   
   .  ... MM . .....  . .               .NMM.,,,,....... .. 
         .NMO.........................MMMM .    .......     
           MMMMMMMMMMMMMMMMMMMMMMMMMMMNZ.. . 
           ''']
rock_rotated = [
'''       ..... .         .  MMMM8 ...                                    
           .........   ..... DMM, IMM....                                   
          ..............?NN=MM~.  .MMNN=..                                  
           .......,..8MMM8NMM,  ..NMMODMM .                                 
               ....,DM?  .. ZMM.,MM=. .,MM..                                
               ...,MM.... .. .MMMO.. ..+MM:.                                
               .. MM .7M:.    .,MM..  MM8IMMD .                             
                .IM$,. DMO.......MM8ZMM....MM:..                            
               ..MM,.,..:NM:..   .MMM$. ...MMM....                          
               . MM.......MMD....=MM:.  .?MMDDMO..                          
               ..MM.. ....$8MMNMMMMMM...MM= ..MM...                         
              . .MM..   .,,DN.++, .~MMMMM. . 8M7..                          
              .  MM.     .IMZ....... .DM:..IMM....                          
            ...IMM . .. .,MM...........MMMMM8..                             
            .,MMO   ..,~MMM.............IMM......                           
         .. MMO.     .DNI...   .  ....?MD? .,,,..                           
        ..IMM          . .      .....DN8.........                           
       ..MMO                . .. ..?MM.........                             
       . IMM. .            ......?MM8..........                             
        . .DMD...          DMMMMMMO..... ........                           
           .IMM=...      $MM~ ......  ..........                            
          ....DMM ..    MM$......      ........                             
               .MM=...8MM..              ...                                
             .  .DMM,MMI . .                .                               
               ... DM+...             ''',
'''       ..,MMM=.             ...                  
         ..DMN,OMM  . ...   ........                
      .. :~MM..  NM8.,. . . .......,.               
     ..MMMMMM?. ..+MMMMMMM..........                
    ..NM~. .DM8..7MM.. .,MMD..,..                   
    ..MM,..  .MMMM:.   ..,?MM ...                   
   .MMMMM... .NMM  .  ....,:M8..                    
 . MM...8MD  MM=.    ..MM$..MM...                   
..~MN.. .+MMMM  ...,.$MD....~M,.                    
...MMMM8.    NMM.....,MD:.,..  M7.                    
. MM..:MM~  .~MMM:..NNMD.,.. ..MN..                   
..MM   .MMMOMMM NMN8MDM:. .. ..MM.                    
.MMO...?MM8... ....NM:     ..MM ..                  
 .7MM .NM..........=MM .    .OMO ...                
 .. NMMM=........,. ZM8 . ....IMM+ ..               
..,..,$MM=..... ...   .MMMM.    .DMM                 
...,....8NO ..,.....  . ...      .,MM?..             
..,.....,ND~....      .. .       . DMM.             
  ....... 8DM  ..  ..              .~MM..           
 ..........,MMM$~,~=            ...MMN ..           
........... . 8MMMMMM?           ~MM.               
 .... ..     ...... DMD. .  . ..MMN.                
   ...             ...MM7 ....ZMM,                  
                      .OMM. .MM$ .                  
                     . ..MMNMM..                    
                        ..7M$ .      '''
]
def printResult(images):
    strings_by_column = [s.split('\n') for s in images]
    strings_by_line = zip(*strings_by_column)
    max_length_by_column = [
        max([len(s) for s in col_strings])
        for col_strings in strings_by_column
    ]
    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i])
            for i in range(len(parts))
        ]
        print(''.join(padded_strings))

def main():
    os.system('cls')
    begin()
    opponent()
    game()

def begin():
    print('Welcome to Rock, Paper, Scissors')
    result = input('Choose either rock, paper or scissors ').lower()
    choicelist = ['rock', 'paper', 'scissors']
    if result in choicelist:
        global pyresult
        pyresult = result
        #print(pyresult)
    else:
        print ('Invalid Selection')
        begin()

def opponent():
    choice = random.randrange(0,3)
    global opresult
    if choice == 0:
        opresult = 'rock'
    elif choice == 1:
        opresult = 'paper'
    else:
        opresult = 'scissors'
    #print(opresult)

def RoShamBo(num):
    print(num)
    printResult(rock_rotated)
    time.sleep(0.25)
    os.system('cls')
    printResult(rock_rock)
    time.sleep(0.25)
    os.system('cls')
    
def game():
    os.system('cls')
    count = 3
    while count>0:
        RoShamBo(count)
        count-=1
    print('Go!')
    printResult(rock_rotated)
    time.sleep(0.25)
    os.system('cls')
    if pyresult == 'rock' and opresult == 'scissors':
        printResult(rock_scissors)
        print("rock beats scissors. You win!")
    elif pyresult == 'rock' and opresult == 'paper':
        printResult(rock_paper)
        print('paper beats rock. You lose.')
    elif pyresult == 'paper' and opresult == 'rock':
        printResult(paper_rock)
        print("paper beats rock. You win!")
    elif pyresult == 'paper' and opresult == 'scissors':
        printResult(paper_scissors)
        print('scissors beat paper. You lose.')
    elif pyresult == 'scissors' and opresult == 'paper':
        printResult(scissors_paper)
        print("scissors beat paper. You win!")
    elif pyresult == 'scissors' and opresult == 'rock':
        printResult(scissors_rock)
        print('rock beats scissors. You lose.')
    elif pyresult == 'rock' and opresult == 'rock':
        printResult(rock_rock)
        print('Same result. Try again.')
    elif pyresult == 'paper' and opresult == 'paper':
        printResult(paper_paper)
        print('Same result. Try again.')
    elif pyresult == 'scissors' and opresult == 'scissors':
        printResult(scissors_scissors)
        print('Same result. Try again.')
    play = input("Play again? (y = Yes, n = No) ").lower()
    if play == 'y':
        main()
    else:
        print("Goodbye!")
        
if __name__=='__main__':
    main()