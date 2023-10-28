// import { NavigationContainer } from "@react-navigation/native";
// import { createStackNavigator } from "@react-navigation/stack";
import { registerRootComponent } from "expo";
import Constants from "expo-constants";
import { StatusBar, StyleSheet, View } from "react-native";
import { Provider } from "react-redux";
import Home from "./src/screens/Home/Home";
import store from "./src/store";

// const Stack = createStackNavigator();

export default function App() {
  return (
    <Provider store={store}>
      <View style={styles.container}>
        {/* <Stack.Navigator>
          <Stack.Screen name="Home" component={Home} />
          <Stack.Screen name="InputNotes" component={InputNotes} /> */}
        {/* </Stack.Navigator> */}
        <Home />
        <StatusBar style="auto" />
      </View>
    </Provider>
  );
}

// export default () => {
//   return (
//     <NavigationContainer>
//       <App />
//     </NavigationContainer>
//   );
// };

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    marginTop: Constants.statusBarHeight,
  },
});

registerRootComponent(App);
