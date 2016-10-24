
//BalanceV5.5 avec arduino


#define pinEnable 13 // Activation du driver/pilote
#define pinStep    9 // Signal de PAS (avancement)
#define pinDir     8 // Direction 

const int buttonPinAvance = 2;
const int buttonPinRecule = 3;
const int photoDiode = 5;  //pin de la photodiode

int buttonStateAvance = 0;
int buttonStateRecule = 0;
int dataPhotoDiode = 0;
int tolerance = 40;
float pas = 0;
float coef = 2.9891;
float poids = 0;
int check = 0;

void setup(){
  Serial.begin(9600);
  
  pinMode( pinEnable, OUTPUT );
  pinMode( pinDir   , OUTPUT );
  pinMode( pinStep  , OUTPUT );
  pinMode(buttonPinAvance, INPUT);
  pinMode(buttonPinRecule, INPUT);
  
}

void loop(){
  
  buttonStateAvance = digitalRead(buttonPinAvance); //Direction Descendre
  buttonStateRecule = digitalRead(buttonPinRecule); //Direction Monter
  
  dataPhotoDiode = analogRead(A0); // 0 obturé 1024 ouvert
  
  //delay(1000);

  if ( ( dataPhotoDiode > ( 512 + tolerance ) ) || ( buttonStateAvance == LOW && buttonStateRecule == HIGH ) )  {
    
    digitalWrite( pinDir   , HIGH); // Direction avant
    digitalWrite( pinStep  , LOW);  // Initialisation de la broche step
  
    digitalWrite( pinStep, HIGH );
    delay( 1 );
    digitalWrite( pinStep, LOW );
    delay( 1 );
    pas += 1;
    Serial.println( pas );
    check = 0;
  }
  else if ( ( dataPhotoDiode < ( 512 - tolerance ) ) || ( buttonStateAvance == HIGH && buttonStateRecule == LOW ) )  {

    digitalWrite( pinDir   , LOW); // Direction avant
  
    digitalWrite( pinStep, HIGH );
    delay( 1 );
    digitalWrite( pinStep, LOW );
    delay( 1 );
    pas -= 1;
    Serial.println( pas );
    check = 0;
  } 
  else { 
    
    if ( check == 0 ) {
       Serial.println( "---Debut Resultat--" );
       Serial.println( "PhotoDiode" );
       Serial.println( dataPhotoDiode );
       poids = pas * coef;
       Serial.println( "PAS" );
       Serial.println( pas );
       Serial.println( "Poids" );
       Serial.println( poids );
       Serial.println( "---Fin Resultat---" );
       check = 1;
    }
    else {
       //pas = 0; 
       //poids = 0;
    }

  }
 
}


