import LottieView from "lottie-react-native";
import React from "react";
import { StyleSheet, View } from "react-native";

function AppLoader() {
  return (
    <View style={[StyleSheet.absoluteFillObject, styles.container]}>
      <LottieView source={require("../../assets/load.json")} 
      autoPlay 
      loop 
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.3)",
    zIndex: 1,
  },
});

export default AppLoader;
