import streamlit as st
import random

# Function to deal a card
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    return random.choice(cards)

# Function to calculate the total value of the hand
def calculate_hand(hand):
    total = sum(hand)
    # Check for aces
    if 11 in hand and total > 21:
        total -= 10
    return total

# Function to check if a hand is a Blackjack (21 with only 2 cards)
def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand(hand) == 21

# Main function to play the game
def play_blackjack():
    st.title("Charlo's Blackjack")
    st.subheader("Gamers never get old!")

    player_hand = []
    dealer_hand = []

    # Betting
    bet = st.number_input("Place your bet:", min_value=1, value=10, step=1)
    st.write(f"Your bet: {bet}")

    # Initial deal
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

    st.write(f"Player's Hand: {player_hand}, Total: {calculate_hand(player_hand)}")
    st.write(f"Dealer's Hand: [{dealer_hand[0]}, ?]")

    # Player's turn
    while calculate_hand(player_hand) < 21:
        action = st.selectbox("Choose an action:", ('Hit', 'Stand'))
        if action == 'Hit':
            player_hand.append(deal_card())
            st.write(f"Player hits. Player's Hand: {player_hand}, Total: {calculate_hand(player_hand)}")
        else:
            st.write(f"Player stands with a total of {calculate_hand(player_hand)}")
            break

    # Dealer's turn
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        st.write(f"Dealer hits. Dealer's Hand: {dealer_hand}, Total: {calculate_hand(dealer_hand)}")

    # Determine the winner
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if player_total > 21:
        st.write("Player busts! Dealer wins.")
        return -bet
    elif dealer_total > 21:
        st.write("Dealer busts! Player wins.")
        return bet
    elif player_total == dealer_total:
        st.write("It's a tie!")
        return 0
    elif player_total == 21 or len(player_hand) == 2 and dealer_total != 21:
        st.write("Blackjack! Player wins.")
        return bet * 1.5
    elif dealer_total == 21 or len(dealer_hand) == 2 and player_total != 21:
        st.write("Blackjack! Dealer wins.")
        return -bet
    elif player_total > dealer_total:
        st.write("Player wins!")
        return bet
    else:
        st.write("Dealer wins!")
        return -bet

# Function to track win/loss history
def track_win_loss(result):
    if result > 0:
        st.write("You won this round!")
    elif result == 0:
        st.write("It's a tie!")
    else:
        st.write("You lost this round.")

# Main function to run the game loop
def main():
    st.sidebar.title("Blackjack")
    win_loss_history = []

    while True:
        result = play_blackjack()
        track_win_loss(result)
        win_loss_history.append(result)
        st.sidebar.write("Win/Loss History:", win_loss_history)

        play_again = st.sidebar.button("Play Again")
        if not play_again:
            st.sidebar.write("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    main()
