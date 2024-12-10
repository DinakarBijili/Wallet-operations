// Function to show User Dashboard and hide Admin Dashboard
const showUserDashboard = () => {
    document.getElementById("user-dashboard").style.display = "block";
    document.getElementById("admin-dashboard").style.display = "none";
};

// Function to show Admin Dashboard and hide User Dashboard
const showAdminDashboard = () => {
    document.getElementById("admin-dashboard").style.display = "block";
    document.getElementById("user-dashboard").style.display = "none";
};

// Register user function
const registerUser = async () => {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone_number = document.getElementById('phone_number').value;

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/register', {
            name: name,
            email: email,
            phone_number: phone_number
        });

        document.getElementById('registration-response').textContent = `Registration successful! Wallet ID: ${response.data.wallet_id}`;
        document.getElementById('registration-response').style.color = 'green';
    } catch (error) {
        document.getElementById('registration-response').textContent = `Error: ${error.response?.data?.error || 'Registration failed'}`;
        document.getElementById('registration-response').style.color = 'red';
    }
};

// Check wallet balance
const checkBalance = async () => {
    const walletId = document.getElementById('wallet_id').value;

    try {
        const response = await axios.get(`http://127.0.0.1:5000/api/wallet/${walletId}/balance`);
        document.getElementById('balance-display').textContent = `Balance: $${response.data.balance}`;
        document.getElementById('balance-display').style.color = 'green';
    } catch (error) {
        document.getElementById('balance-display').textContent = `Error: ${error.response?.data?.error || 'Could not fetch balance'}`;
        document.getElementById('balance-display').style.color = 'red';
    }
};

// Add money to wallet
const addMoney = async () => {
    const wallet_id = document.getElementById('wallet_id').value;
    const amount = document.getElementById('add-money-amount').value;

    if (amount <= 0) {
        document.getElementById('registration-response').textContent = "Please enter a valid amount.";
        document.getElementById('registration-response').style.color = 'red';
        return;
    }

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/wallet/add-money', {
            wallet_id: wallet_id,
            amount: amount,
        });

        document.getElementById('registration-response').textContent = `Money added successfully! New Balance: $${response.data.balance}`;
        document.getElementById('registration-response').style.color = 'green';
    } catch (error) {
        document.getElementById('registration-response').textContent = `Error: ${error.response?.data?.error || 'Add money failed'}`;
        document.getElementById('registration-response').style.color = 'red';
    }
};

// View transaction history
const viewTransactions = async () => {
    const walletId = document.getElementById('wallet_id').value;

    try {
        const response = await axios.get(`http://127.0.0.1:5000/api/wallet/${walletId}/transactions`);
        const transactions = response.data;

        const transactionList = document.getElementById('transaction-list');
        transactionList.innerHTML = '';  // Clear any existing list

        transactions.forEach(transaction => {
            const li = document.createElement('li');
            li.textContent = `${transaction.transaction_type} of $${transaction.amount} at ${new Date(transaction.timestamp).toLocaleString()}`;
            transactionList.appendChild(li);
        });
    } catch (error) {
        document.getElementById('transaction-list').textContent = `Error: ${error.response?.data?.error || 'Could not fetch transactions'}`;
    }
};

// View all wallets (Admin)
const viewAllWallets = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/api/admin/wallets');
        const wallets = response.data;

        const walletList = document.getElementById('wallet-list');
        walletList.innerHTML = '';  // Clear existing list

        wallets.forEach(wallet => {
            const li = document.createElement('li');
            li.textContent = `Wallet ID: ${wallet.wallet_id}, Name: ${wallet.name}, Balance: $${wallet.balance}`;
            walletList.appendChild(li);
        });
    } catch (error) {
        document.getElementById('wallet-list').textContent = `Error: ${error.response?.data?.error || 'Could not fetch wallets'}`;
    }
};

// View all transactions (Admin)
const viewAllTransactions = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/api/admin/transactions');
        const transactions = response.data;

        const transactionList = document.getElementById('all-transaction-list');
        transactionList.innerHTML = '';  // Clear existing list

        transactions.forEach(transaction => {
            const li = document.createElement('li');
            li.textContent = `${transaction.transaction_type} of $${transaction.amount} at ${new Date(transaction.timestamp).toLocaleString()}`;
            transactionList.appendChild(li);
        });
    } catch (error) {
        document.getElementById('all-transaction-list').textContent = `Error: ${error.response?.data?.error || 'Could not fetch transactions'}`;
    }
};
