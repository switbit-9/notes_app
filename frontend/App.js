import Constants from "expo-constants";
import { StatusBar, StyleSheet, View } from "react-native";
import { Provider } from "react-redux";
import Home from "./src/screens/Home/Home";
import store from "./src/store";

export default function App() {
  return (
    <Provider store={store}>
      <View style={styles.container}>

        <Home />
        <StatusBar style="auto" />
      </View>
    </Provider>
  );
}



const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    marginTop: Constants.statusBarHeight,
  },
});

