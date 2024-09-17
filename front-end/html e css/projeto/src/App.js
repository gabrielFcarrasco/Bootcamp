
import Input from './components/input';
import Button from './components/botao';
import { Container, Content, Row } from './styles';
import { useState  } from 'react'; 

const App = () => {
  
  const [currentNumber, setCurrentNumber] = useState('0');
  const [firstNumber, setFirstNumber] = useState('0');
  const [operation, setOperation] = useState('')

  const handleAppNumber = (num) => {
    setCurrentNumber(prev => `${prev === '0' ? '' : prev}${num}`)
  }

  const handleOnClear = () => { 
    setCurrentNumber('0');
    setFirstNumber('0');
    setOperation('');
  }

  const handleSumNumber = () => {

    if(firstNumber === '0'){
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('+');
    }else{
      const sum = Number(firstNumber) + Number(currentNumber);
      setCurrentNumber(String(sum));
      setOperation('')
    }
  }

  const handleSubNumber = () => {

    if(firstNumber === '0'){
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('-');
    }else{
      const sum = Number(firstNumber) - Number(currentNumber);
      setCurrentNumber(String(sum));
      setOperation('')
    }
  }

  const handleDivNumber = () => {

    if(firstNumber === '0'){
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('/');
    }else{
      const sum = Number(firstNumber) / Number(currentNumber);
      setCurrentNumber(String(sum));
      setOperation('')
    }
  }

  const handleMultNumber = () => {

    if(firstNumber === '0'){
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('*');
    }else{
      const sum = Number(firstNumber) * Number(currentNumber);
      setCurrentNumber(String(sum));
      setOperation('')
    }
  }

  const handleEquals = () => {

    if(firstNumber !== '0' && operation !== '' && currentNumber !== '0'){
      switch(operation){
        case '+':
          handleSumNumber();
        break;

        case '-':
          handleSubNumber();
        break;

        case '/':
          handleDivNumber();
        break;

        case '*':
          handleMultNumber();
        break;

        default: break;
      }
    }
  }

  return (
    <Container>
      <Content>
        <Input value={currentNumber}/>
        <Row>
          <Button label="/" onClick={handleDivNumber}/>
          <Button label="C" onClick={handleOnClear}/>
        </Row>
        <Row>
          <Button label="7" onClick={() => handleAppNumber('7')}/>
          <Button label="8" onClick={() => handleAppNumber('8')}/>
          <Button label="9" onClick={() => handleAppNumber('9')}/>
          <Button label="x" onClick={handleMultNumber}/>
        </Row>
        <Row>
        <Button label="4" onClick={() => handleAppNumber('4')}/>
        <Button label="5" onClick={() => handleAppNumber('5')}/>
        <Button label="6" onClick={() => handleAppNumber('6')}/>
        <Button label="-" onClick={handleSubNumber}/>
        </Row>
        <Row>
        <Button label="1" onClick={() => handleAppNumber('1')}/>
        <Button label="2" onClick={() => handleAppNumber('2')}/>
        <Button label="3" onClick={() => handleAppNumber('3')}/>
        <Button label="+" onClick={handleSumNumber}/>
        </Row>
        <Row>
        <Button label="0" onClick={() => handleAppNumber(0)}/>
        <Button label="=" onClick={handleEquals}/>
        </Row>
      </Content>
    </Container>
  );
}

export default App;
