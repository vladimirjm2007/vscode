import React, { useState } from 'react';
import { Send, ArrowDownCircle, ArrowUpCircle, FileText, CreditCard, Calculator, LogOut } from 'lucide-react';

export default function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [transferAmount, setTransferAmount] = useState('');
  const [transferRecipient, setTransferRecipient] = useState('usuario2');
  const [loanAmount, setLoanAmount] = useState('');
  const [accounts, setAccounts] = useState([
    {
      username: 'usuario1',
      password: '1234',
      account: {
        balance: 5000.00,
        transactions: [
          { id: 1, type: 'deposit', amount: 5000.00, date: '2023-10-01', description: 'Initial deposit' }
        ],
        loans: []
      }
    },
    {
      username: 'usuario2',
      password: '1234',
      account: {
        balance: 3000.00,
        transactions: [
          { id: 2, type: 'deposit', amount: 3000.00, date: '2023-10-01', description: 'Initial deposit' }
        ],
        loans: []
      }
    }
  ]);

  const handleLogin = (e) => {
    e.preventDefault();
    const { username, password } = e.target;
    const user = accounts.find(u => 
      u.username === username.value && u.password === password.value
    );
    
    if (user) {
      setCurrentUser(user);
    } else {
      alert('Credenciales inválidas. Intente usuario1/1234 o usuario2/1234');
    }
  };

  const handleTransfer = (e) => {
    e.preventDefault();
    const amount = parseFloat(transferAmount);
    if (isNaN(amount) || amount <= 0) {
      alert('Monto inválido');
      return;
    }
    
    const sender = currentUser;
    const recipient = accounts.find(a => a.username === transferRecipient);
    if (!recipient) {
      alert('Destinatario no encontrado');
      return;
    }
    
    if (sender.account.balance < amount) {
      alert('Fondos insuficientes');
      return;
    }
    
    const newSenderAccount = {
      ...sender.account,
      balance: sender.account.balance - amount,
      transactions: [
        ...sender.account.transactions,
        {
          id: Date.now(),
          type: 'transfer_out',
          amount,
          date: new Date().toISOString().split('T')[0],
          recipient: transferRecipient
        }
      ]
    };
    
    const newRecipientAccount = {
      ...recipient.account,
      balance: recipient.account.balance + amount,
      transactions: [
        ...recipient.account.transactions,
        {
          id: Date.now() + 1,
          type: 'transfer_in',
          amount,
          date: new Date().toISOString().split('T')[0],
          sender: sender.username
        }
      ]
    };
    
    setAccounts(prev => prev.map(account => 
      account.username === sender.username 
        ? { ...account, account: newSenderAccount } 
        : account.username === recipient.username 
          ? { ...account, account: newRecipientAccount } 
          : account
    ));
    
    setTransferAmount('');
    alert(`Transferencia de $${amount.toFixed(2)} realizada con éxito`);
  };

  const handleApplyLoan = (e) => {
    e.preventDefault();
    const amount = parseFloat(loanAmount);
    if (isNaN(amount) || amount <= 0) {
      alert('Monto de préstamo inválido');
      return;
    }
    
    const newLoan = {
      id: Date.now(),
      amount,
      monthlyPayment: amount * 0.05,
      remaining: amount,
      startDate: new Date().toISOString().split('T')[0]
    };
    
    setAccounts(prev => prev.map(account => 
      account.username === currentUser.username 
        ? {
            ...account,
            account: {
              ...account.account,
              loans: [...account.account.loans, newLoan],
              balance: account.account.balance + amount,
              transactions: [
                ...account.account.transactions,
                {
                  id: Date.now() + 2,
                  type: 'loan',
                  amount,
                  date: new Date().toISOString().split('T')[0],
                  description: `Préstamo aprobado - Cuota mensual: $${(amount * 0.05).toFixed(2)}`
                }
              ]
            }
          } 
        : account
    ));
    
    setLoanAmount('');
    alert(`Préstamo de $${amount.toFixed(2)} aprobado con éxito`);
  };

  const handleProcessMonthlyCharges = () => {
    const taxRate = 0.08; // 8% de impuestos
    const userAccount = accounts.find(a => a.username === currentUser.username).account;
    let newBalance = userAccount.balance;
    const newTransactions = [...userAccount.transactions];
    const newLoans = [...userAccount.loans];
    
    // Calcular impuestos
    const taxAmount = newBalance * taxRate;
    newBalance -= taxAmount;
    newTransactions.push({
      id: Date.now(),
      type: 'tax',
      amount: taxAmount,
      date: new Date().toISOString().split('T')[0],
      description: `Impuestos mensuales (${(taxRate * 100).toFixed(0)}%)`
    });
    
    // Procesar préstamos
    newLoans.forEach(loan => {
      const payment = Math.min(loan.monthlyPayment, loan.remaining);
      newBalance -= payment;
      loan.remaining -= payment;
      
      if (payment > 0) {
        newTransactions.push({
          id: Date.now() + loan.id,
          type: 'loan_payment',
          amount: payment,
          date: new Date().toISOString().split('T')[0],
          description: `Abono a préstamo #${loan.id}`
        });
      }
    });
    
    setAccounts(prev => prev.map(account => 
      account.username === currentUser.username 
        ? {
            ...account,
            account: {
              ...account.account,
              balance: newBalance,
              transactions: newTransactions,
              loans: newLoans.filter(loan => loan.remaining > 0)
            }
          } 
        : account
    ));
    
    alert('Procesamiento mensual completado: Impuestos y pagos de préstamos aplicados');
  };

  const handleLogout = () => {
    setCurrentUser(null);
  };

  if (!currentUser) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-md">
          <div className="bg-white py-8 px-4 shadow-xl rounded-2xl sm:px-10">
            <div className="text-center">
              <div className="bg-indigo-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <FileText className="h-8 w-8 text-white" />
              </div>
              <h2 className="mt-2 text-3xl font-bold text-gray-900">Banca Digital</h2>
              <p className="mt-2 text-sm text-gray-600">Sistema de gestión financiera avanzada</p>
            </div>

            <form className="mt-8 space-y-6" onSubmit={handleLogin}>
              <div className="rounded-md shadow-sm -space-y-px">
                <div>
                  <label htmlFor="username" className="sr-only">Usuario</label>
                  <input
                    id="username"
                    name="username"
                    type="text"
                    required
                    className="appearance-none rounded-t-lg relative block w-full px-4 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                    placeholder="Usuario (usuario1 o usuario2)"
                  />
                </div>
                <div>
                  <label htmlFor="password" className="sr-only">Contraseña</label>
                  <input
                    id="password"
                    name="password"
                    type="password"
                    required
                    className="appearance-none rounded-b-lg relative block w-full px-4 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                    placeholder="Contraseña (1234)"
                  />
                </div>
              </div>

              <div>
                <button
                  type="submit"
                  className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-200"
                >
                  Iniciar Sesión
                </button>
              </div>
              
              <div className="text-center text-sm text-gray-500">
                <p>Pruebe con:</p>
                <p className="font-medium">usuario1 / 1234</p>
                <p className="font-medium">usuario2 / 1234</p>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }

  const userAccount = accounts.find(a => a.username === currentUser.username).account;
  const formattedBalance = userAccount.balance.toLocaleString('es-ES', { 
    style: 'currency', 
    currency: 'USD',
    minimumFractionDigits: 2 
  });

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <div className="flex items-center">
            <div className="bg-indigo-600 w-10 h-10 rounded-lg flex items-center justify-center mr-3">
              <FileText className="h-5 w-5 text-white" />
            </div>
            <h1 className="text-xl font-bold text-gray-900">Banca Digital - {currentUser.username}</h1>
          </div>
          <button
            onClick={handleLogout}
            className="flex items-center text-gray-600 hover:text-gray-900 transition-colors"
          >
            <LogOut className="h-5 w-5 mr-1" />
            Cerrar sesión
          </button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Balance Card */}
          <div className="lg:col-span-1">
            <div className="bg-gradient-to-r from-indigo-600 to-purple-600 rounded-2xl shadow-xl overflow-hidden">
              <div className="p-6">
                <h2 className="text-xl font-semibold text-white">Saldo Disponible</h2>
                <p className="mt-4 text-3xl font-bold text-white">{formattedBalance}</p>
                <div className="mt-6 grid grid-cols-2 gap-4">
                  <button
                    onClick={handleProcessMonthlyCharges}
                    className="w-full bg-white text-indigo-600 hover:bg-indigo-50 font-medium py-2 px-4 rounded-lg transition-colors"
                  >
                    Procesar Mensual
                  </button>
                  <button
                    onClick={() => setAccounts(prev => {
                      const user = prev.find(a => a.username === currentUser.username);
                      return prev.map(a => 
                        a.username === currentUser.username 
                          ? { 
                              ...a, 
                              account: {
                                ...a.account,
                                transactions: a.account.transactions.slice(-10)
                              }
                            } 
                          : a
                      );
                    })}
                    className="w-full bg-indigo-700 text-white hover:bg-indigo-800 font-medium py-2 px-4 rounded-lg transition-colors"
                  >
                    Estado de Cuenta
                  </button>
                </div>
              </div>
            </div>

            {/* Loan Application */}
            <div className="mt-6 bg-white rounded-2xl shadow overflow-hidden">
              <div className="p-6">
                <div className="flex items-center mb-4">
                  <CreditCard className="h-5 w-5 text-indigo-600 mr-2" />
                  <h2 className="text-lg font-semibold text-gray-900">Solicitar Préstamo</h2>
                </div>
                <form onSubmit={handleApplyLoan} className="space-y-4">
                  <div>
                    <label htmlFor="loanAmount" className="block text-sm font-medium text-gray-700">
                      Monto solicitado
                    </label>
                    <div className="mt-1 relative rounded-md shadow-sm">
                      <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                        <span className="text-gray-500 sm:text-sm">$</span>
                      </div>
                      <input
                        type="number"
                        name="loanAmount"
                        id="loanAmount"
                        value={loanAmount}
                        onChange={(e) => setLoanAmount(e.target.value)}
                        className="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
                        placeholder="1000"
                        min="100"
                        step="100"
                        required
                      />
                    </div>
                  </div>
                  <button
                    type="submit"
                    className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Solicitar Préstamo
                  </button>
                </form>
                
                {userAccount.loans.length > 0 && (
                  <div className="mt-6 pt-6 border-t border-gray-200">
                    <h3 className="text-sm font-medium text-gray-900 mb-3">Préstamos Activos</h3>
                    {userAccount.loans.map(loan => {
                      const progress = ((loan.amount - loan.remaining) / loan.amount) * 100;
                      return (
                        <div key={loan.id} className="mb-4">
                          <div className="flex justify-between text-sm mb-1">
                            <span className="font-medium">${loan.amount.toFixed(2)}</span>
                            <span className="text-gray-500">{progress.toFixed(0)}% pagado</span>
                          </div>
                          <div className="w-full bg-gray-200 rounded-full h-2">
                            <div 
                              className="bg-indigo-600 h-2 rounded-full" 
                              style={{ width: `${progress}%` }}
                            ></div>
                          </div>
                          <p className="mt-1 text-xs text-gray-500">
                            Cuota mensual: ${loan.monthlyPayment.toFixed(2)}
                          </p>
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-2">
            {/* Transfer Form */}
            <div className="bg-white rounded-2xl shadow overflow-hidden">
              <div className="p-6">
                <div className="flex items-center mb-4">
                  <Send className="h-5 w-5 text-indigo-600 mr-2" />
                  <h2 className="text-lg font-semibold text-gray-900">Realizar Transferencia</h2>
                </div>
                <form onSubmit={handleTransfer} className="space-y-4">
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label htmlFor="recipient" className="block text-sm font-medium text-gray-700">
                        Destinatario
                      </label>
                      <select
                        id="recipient"
                        value={transferRecipient}
                        onChange={(e) => setTransferRecipient(e.target.value)}
                        className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                      >
                        <option value="usuario1">usuario1</option>
                        <option value="usuario2">usuario2</option>
                      </select>
                    </div>
                    <div>
                      <label htmlFor="amount" className="block text-sm font-medium text-gray-700">
                        Monto
                      </label>
                      <div className="mt-1 relative rounded-md shadow-sm">
                        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                          <span className="text-gray-500 sm:text-sm">$</span>
                        </div>
                        <input
                          type="number"
                          name="amount"
                          id="amount"
                          value={transferAmount}
                          onChange={(e) => setTransferAmount(e.target.value)}
                          className="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
                          placeholder="100.00"
                          min="0.01"
                          step="0.01"
                          required
                        />
                      </div>
                    </div>
                  </div>
                  <button
                    type="submit"
                    className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Transferir
                  </button>
                </form>
              </div>
            </div>

            {/* Transaction History */}
            <div className="mt-6 bg-white rounded-2xl shadow overflow-hidden">
              <div className="p-6">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center">
                    <FileText className="h-5 w-5 text-indigo-600 mr-2" />
                    <h2 className="text-lg font-semibold text-gray-900">Historial de Transacciones</h2>
                  </div>
                  <span className="text-sm text-gray-500">
                    Últimas {userAccount.transactions.length} transacciones
                  </span>
                </div>
                
                <div className="flow-root">
                  <ul className="-my-3 divide-y divide-gray-200">
                    {userAccount.transactions.slice().reverse().map((transaction) => (
                      <li key={transaction.id} className="py-3">
                        <div className="flex items-center justify-between">
                          <div className="flex items-center">
                            {transaction.type === 'transfer_in' && (
                              <ArrowDownCircle className="h-5 w-5 text-green-500 mr-2" />
                            )}
                            {transaction.type === 'transfer_out' && (
                              <ArrowUpCircle className="h-5 w-5 text-red-500 mr-2" />
                            )}
                            {transaction.type === 'tax' && (
                              <Calculator className="h-5 w-5 text-blue-500 mr-2" />
                            )}
                            {transaction.type === 'loan' && (
                              <CreditCard className="h-5 w-5 text-purple-500 mr-2" />
                            )}
                            {transaction.type === 'loan_payment' && (
                              <CreditCard className="h-5 w-5 text-indigo-500 mr-2" />
                            )}
                            
                            <div>
                              <p className="text-sm font-medium text-gray-900">
                                {transaction.type === 'transfer_in' && `Transferencia recibida de ${transaction.sender}`}
                                {transaction.type === 'transfer_out' && `Transferencia a ${transaction.recipient}`}
                                {transaction.type === 'tax' && 'Pago de impuestos'}
                                {transaction.type === 'loan' && 'Préstamo aprobado'}
                                {transaction.type === 'loan_payment' && 'Abono a préstamo'}
                                {transaction.description && ` - ${transaction.description}`}
                              </p>
                              <p className="text-xs text-gray-500">{transaction.date}</p>
                            </div>
                          </div>
                          <span className={`text-sm font-semibold ${
                            transaction.type === 'transfer_in' ? 'text-green-600' : 
                            transaction.type === 'loan' ? 'text-purple-600' : 'text-red-600'
                          }`}>
                            {transaction.type === 'transfer_in' ? '+' : ''}${Math.abs(transaction.amount).toLocaleString('es-ES', { 
                              style: 'currency', 
                              currency: 'USD',
                              minimumFractionDigits: 2 
                            })}
                          </span>
                        </div>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}