import LottieView from "lottie-react-native";
import React from "react";
import { StyleSheet, View } from "react-native";
import styles from "./styles";

function AppLoader() {
  return (
    <View style={[StyleSheet.absoluteFillObject, styles.container]}>
      <LottieView source={require("../../assets/load.json")} autoPlay loop />
    </View>
  );
}

export default AppLoader;
