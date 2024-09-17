
import Input from './components/input';
import Button from './components/botao';
import { Container, Content, Row } from './styles';
import { useState  } from 'react'; 

const App = () => {
  
  const [currentNumber, setCurrentNumber] = useState('0');

  const handleAppNumber = (number) => {
    setCurrentNumber(prev => `${number} ${prev}`)
  }

  return (
    <Container>
      <Content>
        <Input value={currentNumber}/>
        <Row>
          <Button label="/" onClick={() => handleAppNumber('')}/>
          <Button label="C" onClick={() => handleAppNumber('')}/>
        </Row>
        <Row>
          <Button label="7" onClick={() => handleAppNumber('')}/>
          <Button label="8" onClick={() => handleAppNumber('')}/>
          <Button label="9" onClick={() => handleAppNumber('')}/>
          <Button label="x" onClick={() => handleAppNumber('')}/>
        </Row>
        <Row>
        <Button label="4" onClick={() => handleAppNumber('')}/>
        <Button label="5" onClick={() => handleAppNumber('')}/>
        <Button label="6" onClick={() => handleAppNumber('')}/>
        <Button label="-" onClick={() => handleAppNumber('')}/>
        </Row>
        <Row>
        <Button label="1" onClick={() => handleAppNumber('')}/>
        <Button label="2" onClick={() => handleAppNumber('')}/>
        <Button label="3" onClick={() => handleAppNumber('')}/>
        <Button label="+" onClick={() => handleAppNumber('+')}/>
        </Row>
        <Row>
        <Button label="0" onClick={() => handleAppNumber('0')}/>
        <Button label="=" onClick={() => handleAppNumber('')}/>
        </Row>
      </Content>
    </Container>
  );
}

export default App;
