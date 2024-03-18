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
    st.title("Chaplin's Blackjack")
    st.subheader("A game a day, keeps boredom away!")

    player_hand = []
    dealer_hand = []

    # Initial deal
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

    st.write(f"Player's Hand: {player_hand}, Total: {calculate_hand(player_hand)}")
    st.write(f"Dealer's Hand: [{dealer_hand[0]}, ?]")

    # Player's turn
    while calculate_hand(player_hand) < 21:
        action = st.radio("Choose an action:", ('Hit', 'Stand'))
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
    elif dealer_total > 21:
        st.write("Dealer busts! Player wins.")
    elif player_total == dealer_total:
        st.write("It's a tie!")
    elif player_total == 21 or len(player_hand) == 2 and dealer_total != 21:
        st.write("Blackjack! Player wins.")
    elif dealer_total == 21 or len(dealer_hand) == 2 and player_total != 21:
        st.write("Blackjack! Dealer wins.")
    elif player_total > dealer_total:
        st.write("Player wins!")
    else:
        st.write("Dealer wins!")

# Run the game
if __name__ == "__main__":
    play_blackjack()
